from statistics import median
from typing import Any

from gradebotguru.llm_interface.base_llm import BaseLLM
from gradebotguru.prompts import generate_prompt
from gradebotguru.response_parser import parse_response
from gradebotguru.text_analysis import analyze_sentiment, analyze_style


def summarize(feedback: list[str], llm: BaseLLM) -> str:
    """
    Summarize feedback using the best LLM provider.

    Args:
        feedback (List[str]): List of feedback.
        llm (BaseLLM): The best LLM provider.

    Returns:
        str: Summarized feedback.
    """
    feedback_summary = " ".join(feedback)
    summary_prompt = f'Summarize this feedback into one concise paragraph as if you are talking directly to the student, so use "you" instead of "the student": {feedback_summary}'
    summary = llm.generate_text(summary_prompt)
    return summary


def grade_submission(
    submission_id: str,
    submission: str,
    rubric: dict[str, dict[str, Any]],
    llms: list[BaseLLM],
    num_repeats: int,
    repeat_each_provider: bool,
    aggregation_method: str,
    bias_adjustments: dict[str, float] | None = None,
    prompt_template: str = "Grade the following student submission based on the rubric provided. The rubric is as follows: \n\n {rubric}. \n\n The student submission is as follows: \n\n {submission}.",
    summarize_feedback: bool = False,
) -> dict[str, Any]:
    """
    Grade a student submission using multiple LLM providers and repeats.

    Args:
        submission_id (str): The ID of the student submission.
        submission (str): The student submission text.
        rubric (Dict[str, Dict[str, Any]]): The grading rubric.
        llms (List[BaseLLM]): List of LLM providers.
        num_repeats: Number of times to repeat the grading process.
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
            llm,
            submission,
            rubric,
            num_repeats,
            repeat_each_provider,
            prompt_template,
            bias_adjustments,
        )
        all_individual_responses.extend(individual_responses)
        all_grades.extend(provider_grades)
        for response in individual_responses:
            provider_info_str = " ".join(
                f"{k}: {v}" for k, v in response["provider_info"].items()
            )
            providers_info.add(provider_info_str)

    aggregated_response = aggregate_responses(
        all_individual_responses,
        aggregation_method,
        llms,
        num_repeats,
        repeat_each_provider,
        summarize_feedback,
    )
    overall_grade = sum(
        criterion["grade"] for criterion in aggregated_response["criteria"]
    )

    return create_result_dict(
        submission_id,
        submission,
        rubric,
        overall_grade,
        aggregated_response,
        providers_info,
        all_individual_responses,
    )


def run_evaluations(
    llm: BaseLLM,
    submission: str,
    rubric: dict[str, Any],
    num_repeats: int,
    repeat_each_provider: bool,
    prompt_template: str,
    bias_adjustments: dict[str, float] | None,
) -> tuple[list[dict[str, Any]], list[float]]:
    """
    Run evaluations for a given LLM.

    Args:
        llm (BaseLLM): The LLM provider.
        submission (str): The student submission text.
        rubric (Dict[str, Any]): The grading rubric.
        num_repeats: Number of times to repeat the grading process.
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
        total_grade = sum(criterion["grade"] for criterion in criteria)

        individual_responses.append(
            {
                "criteria": criteria,
                "overall_feedback": overall_feedback,
                "provider_info": llm.get_model_info(),
                "iteration": i + 1,
            }
        )
        provider_grades.append(total_grade)

    return individual_responses, provider_grades


def aggregate_responses(
    responses: list[dict[str, Any]],
    aggregation_method: str,
    llms: list[BaseLLM],
    num_repeats: int,
    repeat_each_provider: bool,
    summarize_feedback: bool,
) -> dict[str, Any]:
    """
    Aggregate responses from multiple evaluations.

    Args:
        responses (List[Dict[str, Any]]): List of individual responses.
        aggregation_method (str): The method to aggregate grades.
        llms (List[BaseLLM]): List of LLM providers.
        num_repeats: Number of times to repeat the grading process.
        repeat_each_provider (bool): Whether to repeat grading for each provider.
        summarize_feedback (bool): Whether to summarize feedback from all LLMs.

    Returns:
        Dict[str, Any]: Aggregated response.
    """
    criteria_by_name: dict[str, dict[str, list]] = {}
    all_overall_feedbacks = []
    aggregated_provider_info = set()
    best_llm = max(llms, key=lambda llm: llm.get_model_info().get("weight", 1.0))

    for response in responses:
        all_overall_feedbacks.append(response["overall_feedback"]["overall"])
        for criterion in response["criteria"]:
            name = criterion["name"]
            feedback = criterion["feedback"]
            grade = criterion["grade"]
            if name not in criteria_by_name:
                criteria_by_name[name] = {"feedbacks": [], "grades": []}
            criteria_by_name[name]["feedbacks"].append(feedback)
            criteria_by_name[name]["grades"].append(grade)
        provider_info_str = " ".join(
            f"{k}: {v}" for k, v in response["provider_info"].items()
        )
        aggregated_provider_info.add(provider_info_str)

    aggregated_criteria = []
    for name, feedbacks_grades in criteria_by_name.items():
        aggregated_feedback = " ".join(feedbacks_grades["feedbacks"])
        aggregated_grade = aggregate_grades(
            aggregation_method,
            feedbacks_grades["grades"],
            llms,
            num_repeats,
            repeat_each_provider,
        )
        if summarize_feedback:
            aggregated_feedback = summarize(feedbacks_grades["feedbacks"], best_llm)
        aggregated_criteria.append(
            {"name": name, "feedback": aggregated_feedback, "grade": aggregated_grade}
        )

    aggregated_overall_feedback = " ".join(all_overall_feedbacks)
    if summarize_feedback:
        aggregated_overall_feedback = summarize(all_overall_feedbacks, best_llm)

    return {
        "criteria": aggregated_criteria,
        "overall_feedback": aggregated_overall_feedback,
        "provider_info": list(aggregated_provider_info),
        "iteration": len(responses),
    }


def aggregate_grades(
    aggregation_method: str,
    grades: list[float],
    llms: list[BaseLLM],
    num_repeats: int,
    repeat_each_provider: bool,
) -> float:
    """
    Aggregate grades based on the specified method.

    Args:
        aggregation_method (str): The method to aggregate grades.
        grades (List[float]): List of grades.
        llms (List[BaseLLM]): List of LLM providers.
        num_repeats: Number of times to repeat the grading process.
        repeat_each_provider (bool): Whether to repeat grading for each provider.

    Returns:
        float: The aggregated grade.
    """
    if not grades:
        return 0.0

    if aggregation_method in ["simple_average", "bias_adjusted"]:
        return round((sum(grades) / len(grades)) * 2) / 2  # Round to nearest 0.5
    elif aggregation_method == "weighted_average":
        weights = [
            llm.get_model_info().get("weight", 1.0)
            for llm in llms
            for _ in range(num_repeats if repeat_each_provider else 1)
        ]
        weighted_sum = sum(grade * weight for grade, weight in zip(grades, weights, strict=False))
        result = (weighted_sum / sum(weights))
        return float(round(result * 2) / 2)  # Round to nearest 0.5
    elif aggregation_method == "median":
        return float(median(grades))
    else:
        raise ValueError(f"Unsupported aggregation method: {aggregation_method}")


def create_result_dict(
    submission_id: str,
    submission: str,
    rubric: dict[str, Any],
    overall_grade: float,
    aggregated_response: dict[str, Any],
    providers_info: set,
    individual_responses: list[dict[str, Any]],
) -> dict[str, Any]:
    """
    Create the final result dictionary with all relevant information.

    Args:
        submission_id (str): The ID of the student submission.
        submission (str): The student submission text.
        rubric (Dict[str, Any]): The grading rubric.
        overall_grade: The overall grade for the submission.
        aggregated_response: The aggregated response.
        providers_info (set): Information about the providers.
        individual_responses (List[Dict[str, Any]]): List of individual responses.

    Returns:
        Dict[str, Any]: The final result dictionary.
    """
    sentiment_analysis = analyze_sentiment(submission)
    style = analyze_style(submission)

    return {
        "submission_id": submission_id,
        "word_count": style["word_count"],
        "readability": style["readability"],
        "sentiment": sentiment_analysis,
        "grade": round(overall_grade * 2) / 2
        if overall_grade
        else 0,  # Round to nearest 0.5
        "out_of": sum(details["max_points"] for details in rubric.values()),
        "aggregated_response": aggregated_response,
        "individual_responses": individual_responses,
    }
