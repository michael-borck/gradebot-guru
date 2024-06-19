from typing import Dict, Any, List, Tuple, Optional
from statistics import median
from gradebotguru.llm_interface.base_llm import BaseLLM
from gradebotguru.prompts import generate_prompt
from gradebotguru.text_analysis import analyze_sentiment, analyze_style
from gradebotguru.response_parser import parse_response


def grade_submission(
    submission_id: str,
    submission: str,
    rubric: Dict[str, Dict[str, Any]],
    llms: List[BaseLLM],
    num_repeats: int,
    repeat_each_provider: bool,
    aggregation_method: str,
    bias_adjustments: Optional[Dict[str, float]] = None,
    prompt_template: str = "Grade the following student submission based on the rubric provided. The rubric is as follows: {rubric}. The student submission is as follows: {submission}.",
    summarize_feedback: bool = False
) -> Dict[str, Any]:
    """
    Grade a student submission using multiple LLM providers and repeats.

    Args:
        submission_id (str): The ID of the student submission.
        submission (str): The student submission text.
        rubric (Dict[str, Dict[str, Any]]): The grading rubric.
        llms (List[BaseLLM]): List of LLM providers.
        num_repeats (int): Number of times to repeat the grading process.
        repeat_each_provider (bool): Whether to repeat grading for each provider.
        aggregation_method (str): The method to aggregate grades.
        bias_adjustments (Optional[Dict[str, float]]): Bias adjustments for specific providers.
        prompt_template (str): Custom prompt template for LLMs.
        summarize_feedback (bool): Whether to summarize feedback from all LLMs.

    Returns:
        Dict[str, Any]: Aggregated grading results and individual responses.
    """
    all_individual_responses = []
    all_grades = []
    providers_info = set()

    for llm in llms:
        individual_responses, provider_grades = run_evaluations(
            llm, submission, rubric, num_repeats, repeat_each_provider, prompt_template, bias_adjustments
        )
        all_individual_responses.extend(individual_responses)
        all_grades.extend(provider_grades)
        providers_info.add(" ".join([str(v) for v in llm.get_model_info().values()]))

    aggregated_response = aggregate_responses(
        all_individual_responses, aggregation_method, llms, num_repeats, repeat_each_provider
    )
    overall_grade = sum(criterion['grade'] for criterion in aggregated_response['criteria'])

    return create_result_dict(
        submission_id, submission, rubric, overall_grade, aggregated_response, providers_info, all_individual_responses
    )


def run_evaluations(
    llm: BaseLLM,
    submission: str,
    rubric: Dict[str, Any],
    num_repeats: int,
    repeat_each_provider: bool,
    prompt_template: str,
    bias_adjustments: Optional[Dict[str, float]]
) -> Tuple[List[Dict[str, Any]], List[float]]:
    """
    Run evaluations for a given LLM.

    Args:
        llm (BaseLLM): The LLM provider.
        submission (str): The student submission text.
        rubric (Dict[str, Any]): The grading rubric.
        num_repeats (int): Number of times to repeat the grading process.
        repeat_each_provider (bool): Whether to repeat grading for each provider.
        prompt_template (str): Custom prompt template for LLMs.
        bias_adjustments (Optional[Dict[str, float]]): Bias adjustments for specific providers.

    Returns:
        Tuple[List[Dict[str, Any]], List[float]]: List of individual responses and their grades.
    """
    individual_responses = []
    provider_grades = []
    repeats = num_repeats if repeat_each_provider else 1

    for i in range(repeats):
        prompt = generate_prompt(rubric, submission, prompt_template)
        response = llm.get_response(prompt)
        criteria, overall_feedback = parse_response(response)
        total_grade = sum(criterion['grade'] for criterion in criteria)

        individual_responses.append({
            "criteria": criteria,
            "overall_feedback": overall_feedback,
            "provider_info": llm.get_model_info(),
            "iteration": i + 1
        })
        provider_grades.append(total_grade)

    return individual_responses, provider_grades


def aggregate_responses(
    responses: List[Dict[str, Any]],
    aggregation_method: str,
    llms: List[BaseLLM],
    num_repeats: int,
    repeat_each_provider: bool
) -> Dict[str, Any]:
    """
    Aggregate responses from multiple evaluations.

    Args:
        responses (List[Dict[str, Any]]): List of individual responses.
        aggregation_method (str): The method to aggregate grades.
        llms (List[BaseLLM]): List of LLM providers.
        num_repeats (int): Number of times to repeat the grading process.
        repeat_each_provider (bool): Whether to repeat grading for each provider.

    Returns:
        Dict[str, Any]: Aggregated response.
    """
    criteria_by_name = {}
    all_overall_feedbacks = []

    for response in responses:
        all_overall_feedbacks.append(response['overall_feedback']['overall'])
        for criterion in response['criteria']:
            name = criterion['name']
            feedback = criterion['feedback']
            grade = criterion['grade']
            if name not in criteria_by_name:
                criteria_by_name[name] = {'feedbacks': [], 'grades': []}
            criteria_by_name[name]['feedbacks'].append(feedback)
            criteria_by_name[name]['grades'].append(grade)

    aggregated_criteria = []
    for name, feedbacks_grades in criteria_by_name.items():
        aggregated_feedback = " ".join(feedbacks_grades['feedbacks'])
        aggregated_grade = aggregate_grades(
            aggregation_method, feedbacks_grades['grades'], llms, num_repeats, repeat_each_provider
        )
        aggregated_criteria.append({'name': name, 'feedback': aggregated_feedback, 'grade': aggregated_grade})

    aggregated_overall_feedback = " ".join(all_overall_feedbacks)

    return {
        "criteria": aggregated_criteria,
        "overall_feedback": aggregated_overall_feedback,
        "provider_info": "Aggregated",
        "iteration": len(responses)
    }


def aggregate_grades(
    aggregation_method: str,
    grades: List[float],
    llms: List[BaseLLM],
    num_repeats: int,
    repeat_each_provider: bool
) -> float:
    """
    Aggregate grades based on the specified method.

    Args:
        aggregation_method (str): The method to aggregate grades.
        grades (List[float]): List of grades.
        llms (List[BaseLLM]): List of LLM providers.
        num_repeats (int): Number of times to repeat the grading process.
        repeat_each_provider (bool): Whether to repeat grading for each provider.

    Returns:
        float: The aggregated grade.
    """
    if not grades:
        return 0.0

    if aggregation_method in ["simple_average", "bias_adjusted"]:
        return sum(grades) / len(grades)
    elif aggregation_method == "weighted_average":
        weights = [llm.get_model_info().get('weight', 1.0) for llm in llms for _ in range(num_repeats if repeat_each_provider else 1)]
        weighted_sum = sum(grade * weight for grade, weight in zip(grades, weights))
        return weighted_sum / sum(weights) if weights else None
    elif aggregation_method == "median":
        return median(grades)
    else:
        raise ValueError(f"Unsupported aggregation method: {aggregation_method}")


def create_result_dict(
    submission_id: str,
    submission: str,
    rubric: Dict[str, Any],
    overall_grade: float,
    aggregated_response: Dict[str, Any],
    providers_info: set,
    individual_responses: List[Dict[str, Any]]
) -> Dict[str, Any]:
    """
    Create the final result dictionary with all relevant information.

    Args:
        submission_id (str): The ID of the student submission.
        submission (str): The student submission text.
        rubric (Dict[str, Any]): The grading rubric.
        overall_grade (float): The overall grade for the submission.
        aggregated_response (Dict[str, Any]): The aggregated response.
        providers_info (set): Information about the providers.
        individual_responses (List[Dict[str, Any]]): List of individual responses.

    Returns:
        Dict[str, Any]: The final result dictionary.
    """
    sentiment_analysis = analyze_sentiment(submission)
    style = analyze_style(submission)

    return {
        "submission_id": submission_id,
        "word_count": style['word_count'],
        "readability": style['readability'],
        "sentiment": sentiment_analysis,
        "grade": round(overall_grade * 2) / 2 if overall_grade else 0,  # Round to nearest 0.5
        "out_of": sum(details["max_points"] for details in rubric.values()),
        "aggregated_response": aggregated_response,
        "individual_responses": individual_responses
    }
