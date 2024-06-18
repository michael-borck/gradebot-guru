import re
import logging
from typing import Dict, Any, List, Tuple, Optional
from statistics import median
from gradebotguru.llm_interface.base_llm import BaseLLM
from gradebotguru.prompts import generate_prompt
from gradebotguru.text_analysis import analyze_sentiment, analyze_style
from gradebotguru.response_parser import parse_response


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
    # Keep track of individual grades and feedback for each LLM
    llm_all_grades = []
    llm_all_criterion = []
    llm_all_overall = []
    llm_all_breakdown = []

    for llm in llms:
        # Keep track of individual grades and feedback for each 'repeat' of the grading process
        all_grades = []
        all_criterion = []
        all_overall = []
        all_breakdown = []
        provider_info = set()

        repeats = num_repeats if repeat_each_provider else 1
        for _ in range(repeats):
            prompt = generate_prompt(rubric, submission, prompt_template)
            response = llm.get_response(prompt)
            print(response)
            print('\n\n\n')
            result = parse_response(response)
            breakdown = result.get('breakdown')
            criterion_feedback = result.get('criterion_feedback')
            overall_feedback = result.get('overall_feedback')
            grade = result.get('total_score')

            if aggregation_method == "bias_adjusted" and bias_adjustments:
                llm_info = llm.get_model_info()
                provider_name = llm_info.get("model_name", "")
                grade = (grade or 0) + bias_adjustments.get(provider_name, 0)

            if breakdown:
                all_breakdown.append(breakdown)
            if grade:
                all_grades.append(grade)
            if criterion_feedback:
                all_criterion.append(criterion_feedback)
            if overall_feedback:
                all_overall.append(overall_feedback)

        if repeats > 1:
            all_average_grade = aggregate_results(aggregation_method, all_grades, llms, num_repeats, repeat_each_provider)
            # average_criterion = aggregate_criterion(aggregation_method, all_criterion, llms, num_repeats, repeat_each_provider)
            all_criterion_summary, llm_overall_summary = aggregate_feedback(all_criterion, all_overall, llms)
        else:
            all_average_grade = all_grades[0] if all_grades else None
            all_criterion_summary = all_criterion[0] if all_criterion else None
            all_overall_summary = all_overall[0] if all_overall else None
            # average_criterion = all_criterion[0] if all_criterion else None

        if all_average_grade:
            llm_all_grades.append(all_average_grade)
        if all_criterion_summary:
            llm_all_criterion.append(all_criterion_summary)
        if all_overall_summary:
            llm_all_overall.append(all_overall_summary)

        provider_info.add(" ".join([str(v) for v in llm.get_model_info().values()]))

    if len(llms) > 1:
        llm_average_grade = aggregate_results(aggregation_method, llm_all_grades, llms, num_repeats, repeat_each_provider)
        llm_criterion_summary, llm_overall_summary = aggregate_feedback(llm_all_criterion, llm_all_overall, llms)
    else:
        llm_average_grade = llm_all_grades[0] if llm_all_grades else None
        llm_criterion_summary = llm_all_criterion[0] if llm_all_criterion else None
        llm_overall_summary = llm_all_overall[0] if llm_all_overall else None

    sentiment_analysis = analyze_sentiment(submission)
    style = analyze_style(submission)

    return {
        "providers": provider_info,
        "word_count": style['word_count'],
        "readability": style['readability'],
        "sentiment": sentiment_analysis,
        "grade": round(llm_average_grade * 2) / 2 if llm_average_grade else 0,  # Round to nearest 0.5
        "out_of": sum(details["max_points"] for details in rubric.values()),
        "breakdown": llm_all_grades,
        "criteria_feedback": llm_criterion_summary,
        "feedback": llm_overall_summary,
    }


def aggregate_results(
    aggregation_method: str,
    all_grades: List[float],
    llms: List[BaseLLM],
    num_repeats: int,
    repeat_each_provider: bool
) -> Optional[float]:
    """
    Aggregate grading results based on the specified aggregation method.

    Args:
        aggregation_method (str): The method to aggregate grades.
        all_grades (List[float]): List of grades.
        llms (List[BaseLLM]): List of LLM providers.
        num_repeats (int): Number of times to repeat the grading process.
        repeat_each_provider (bool): Whether to repeat grading for each provider.

    Returns:
        Optional[float]: The aggregated grade.
    """
    if not all_grades:
        return None

    if aggregation_method == "simple_average":
        return sum(all_grades) / len(all_grades)
    elif aggregation_method == "weighted_average":
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
    all_feedback: List[str],
    all_overall_feedback: List[str],
    llms: List[BaseLLM]
) -> Tuple[str, str]:
    """
    Aggregate feedback from multiple LLMs.

    Args:
        all_feedback (List[str]): List of feedback.
        all_overall_feedback (List[str]): List of overall feedback.
        llms (List[BaseLLM]): List of LLM providers.

    Returns:
        Tuple[str, str]: Aggregated feedback summary and overall feedback summary.
    """
    best_llm = sorted(llms, key=lambda llm: llm.get_model_info().get('weight', 1.0), reverse=True)[0]
    feedback_summary = summarize(all_feedback, best_llm) if all_feedback else ''
    overall_feedback_summary = summarize(all_overall_feedback, best_llm) if all_overall_feedback else ''

    return feedback_summary, overall_feedback_summary


def summarize(feedback: List[str], llm: BaseLLM) -> str:
    """
    Summarize feedback using the best LLM provider.

    Args:
        feedback (List[str]): List of feedback.
        llm (BaseLLM): The best LLM provider.

    Returns:
        str: Summarized feedback.
    """
    feedback_summary = ' '.join(feedback)
    summary_prompt = f'Summarize this feedback as if you are talking directly to the student, so use "you" instead of "the student": {feedback_summary}'
    summary = llm.generate_text(summary_prompt, max_length=200)
    return summary
