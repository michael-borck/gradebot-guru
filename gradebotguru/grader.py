import re
import logging
from typing import Dict, Any, List, Tuple, Optional
from statistics import median
from gradebotguru.llm_interface.base_llm import BaseLLM
from gradebotguru.prompts import generate_prompt
from gradebotguru.text_analysis import analyze_sentiment, analyze_style
from gradebotguru.response_parser import parse_response


def process_evaluation(text: str) -> Tuple[List[Dict[str, Any]], Dict[str, int], Dict[str, str], Dict[str, str], int]:
    """
    Process the evaluation by parsing the response and calculating grades.

    Parameters:
    - text (str): The response string from the LLM.

    Returns:
    - Tuple: A tuple containing:
        - List[Dict[str, Any]]: A list of dictionaries for each criterion with keys 'name', 'grade', and 'feedback'.
        - Dict[str, int]: A dictionary with criterion names as keys and grades as values.
        - Dict[str, str]: A dictionary with criterion names as keys and feedback as values.
        - Dict[str, str]: A dictionary with the overall feedback.
        - int: The total grade.
    """
    criteria, overall_feedback = parse_response(text)

    # Extracting criterion grades
    criterion_grades = {criterion['name']: criterion['grade'] for criterion in criteria}

    # Calculate total grade
    total_grade = sum(criterion_grades.values())

    # Extracting criterion feedback
    criterion_feedback = {criterion['name']: criterion['feedback'] for criterion in criteria}

    return criteria, criterion_grades, criterion_feedback, overall_feedback, total_grade

def grade_submission(
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
        Dict[str, Any]: Aggregated grading results.
    """
    llm_all_grades, llm_all_criterion_feedback, llm_all_overall_feedback = [], [], []
    providers_info = set()

    for llm in llms:
        all_grades, all_criterion_feedback, all_overall_feedback = run_evaluations(
            llm, submission, rubric, num_repeats, repeat_each_provider, prompt_template, aggregation_method, bias_adjustments
        )

        aggregate_and_store_results(
            all_grades, all_criterion_feedback, all_overall_feedback, llm_all_grades, llm_all_criterion_feedback, llm_all_overall_feedback
        )

        providers_info.add(" ".join([str(v) for v in llm.get_model_info().values()]))

    llm_average_grade, llm_criterion_feedback_summary, llm_overall_feedback_summary = finalize_aggregations(
        llms, llm_all_grades, llm_all_criterion_feedback, llm_all_overall_feedback, aggregation_method, num_repeats, repeat_each_provider
    )

    return create_result_dict(submission, rubric, llm_average_grade, llm_criterion_feedback_summary, llm_overall_feedback_summary, providers_info)


def run_evaluations(
    llm: BaseLLM, submission: str, rubric: Dict[str, Any], num_repeats: int, repeat_each_provider: bool, prompt_template: str, aggregation_method: str, bias_adjustments: Optional[Dict[str, float]]
) -> Tuple[List[float], List[Dict[str, str]], List[Dict[str, str]]]:
    all_grades, all_criterion_feedback, all_overall_feedback = [], [], []
    repeats = num_repeats if repeat_each_provider else 1

    for _ in range(repeats):
        prompt = generate_prompt(rubric, submission, prompt_template)
        response = llm.get_response(prompt)
        criteria, criterion_grades, criterion_feedback, overall_feedback, total_grade = process_evaluation(response)

        if aggregation_method == "bias_adjusted" and bias_adjustments:
            llm_info = llm.get_model_info()
            provider_name = llm_info.get("model_name", "")
            total_grade += bias_adjustments.get(provider_name, 0)

        all_grades.append(total_grade)
        all_criterion_feedback.append(criterion_feedback)
        all_overall_feedback.append(overall_feedback)

    return all_grades, all_criterion_feedback, all_overall_feedback


def aggregate_and_store_results(
    all_grades: List[float], all_criterion_feedback: List[Dict[str, str]], all_overall_feedback: List[Dict[str, str]],
    llm_all_grades: List[float], llm_all_criterion_feedback: List[Dict[str, str]], llm_all_overall_feedback: List[Dict[str, str]]
):
    average_grade = aggregate_results("simple_average", all_grades)  # Using simple average as an example
    criterion_feedback_summary, overall_feedback_summary = aggregate_feedback(all_criterion_feedback, all_overall_feedback)

    llm_all_grades.append(average_grade)
    llm_all_criterion_feedback.append(criterion_feedback_summary)
    llm_all_overall_feedback.append(overall_feedback_summary)


def finalize_aggregations(
    llms: List[BaseLLM], llm_all_grades: List[float], llm_all_criterion_feedback: List[Dict[str, str]], llm_all_overall_feedback: List[Dict[str, str]],
    aggregation_method: str, num_repeats: int, repeat_each_provider: bool
) -> Tuple[float, Dict[str, str], str]:
    if len(llms) > 1:
        llm_average_grade = aggregate_results(aggregation_method, llm_all_grades, llms, num_repeats, repeat_each_provider)
        llm_criterion_feedback_summary, llm_overall_feedback_summary = aggregate_feedback(llm_all_criterion_feedback, llm_all_overall_feedback, llms)
    else:
        llm_average_grade = llm_all_grades[0] if llm_all_grades else None
        llm_criterion_feedback_summary = llm_all_criterion_feedback[0] if llm_all_criterion_feedback else None
        llm_overall_feedback_summary = llm_all_overall_feedback[0] if llm_all_overall_feedback else None

    return llm_average_grade, llm_criterion_feedback_summary, llm_overall_feedback_summary


def create_result_dict(
    submission: str, rubric: Dict[str, Any], llm_average_grade: float, llm_criterion_feedback_summary: Dict[str, str], llm_overall_feedback_summary: str, providers_info: set
) -> Dict[str, Any]:
    sentiment_analysis = analyze_sentiment(submission)
    style = analyze_style(submission)

    return {
        "providers": list(providers_info),
        "word_count": style['word_count'],
        "readability": style['readability'],
        "sentiment": sentiment_analysis,
        "grade": round(llm_average_grade * 2) / 2 if llm_average_grade else 0,  # Round to nearest 0.5
        "out_of": sum(details["max_points"] for details in rubric.values()),
        "criteria_feedback": llm_criterion_feedback_summary,
        "feedback": llm_overall_feedback_summary,
    }


def aggregate_results(
    aggregation_method: str,
    all_grades: List[float],
    llms: Optional[List[BaseLLM]] = None,
    num_repeats: Optional[int] = None,
    repeat_each_provider: Optional[bool] = None
) -> Optional[float]:
    if not all_grades:
        return None

    if aggregation_method == "simple_average":
        return sum(all_grades) / len(all_grades)
    elif aggregation_method == "weighted_average" and llms:
        weights = [llm.get_model_info().get('weight', 1.0) for llm in llms for _ in range(num_repeats if repeat_each_provider else 1)]
        weighted_sum = sum(grade * weight for grade, weight in zip(all_grades, weights))
        return weighted_sum / sum(weights) if weights else None
    elif aggregation_method == "median":
        return median(all_grades)
    elif aggregation_method == "bias_adjusted":
        return sum(all_grades) / len(all_grades)
    else:
        raise ValueError(f"Unsupported aggregation method: {aggregation_method}")


def aggregate_feedback(
    all_criterion_feedback: List[Dict[str, str]],
    all_overall_feedback: List[Dict[str, str]],
    llms: Optional[List[BaseLLM]] = None
) -> Tuple[Dict[str, str], str]:
    aggregated_criterion_feedback = {}
    aggregated_overall_feedback = ""

    for feedback in all_criterion_feedback:
        for key, value in feedback.items():
            if key not in aggregated_criterion_feedback:
                aggregated_criterion_feedback[key] = []
            aggregated_criterion_feedback[key].append(value)

    for key, feedbacks in aggregated_criterion_feedback.items():
        aggregated_criterion_feedback[key] = " ".join(feedbacks)

    aggregated_overall_feedback = " ".join(
        feedback["overall"] for feedback in all_overall_feedback if "overall" in feedback
    )

    return aggregated_criterion_feedback, aggregated_overall_feedback
