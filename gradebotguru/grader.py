import re
import logging
from typing import Dict, Any, List
from statistics import median
from gradebotguru.llm_interface.base_llm import BaseLLM
from gradebotguru.prompts import generate_prompt
from gradebotguru.text_analysis import analyze_sentiment, analyze_style

def parse_response(response: str) -> Dict[str, Any]:
    """
    Parse the response from the LLM to extract grades and feedback.

    Parameters:
    - response (str): The response string from the LLM.

    Returns:
    - Dict[str, Any]: A dictionary containing the extracted grades and feedback.
    """
    grade_pattern = re.compile(r"Grade:\s*(\d+(\.\d+)?)")
    feedback_pattern = re.compile(r"Feedback:\s*(.+)", re.DOTALL)

    grade_match = grade_pattern.search(response)
    feedback_match = feedback_pattern.search(response)

    grade = float(grade_match.group(1)) if grade_match else None
    feedback = feedback_match.group(1).strip() if feedback_match else None

    return {
        "grade": grade,
        "feedback": feedback
    }

def grade_submission(
    submission: str,
    rubric: Dict[str, Dict[str, Any]],
    llms: List[BaseLLM],
    num_repeats: int,
    repeat_each_provider: bool,
    aggregation_method: str,
    bias_adjustments: Dict[str, float] = None,
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
        bias_adjustments (Dict[str, float]): Bias adjustments for specific providers.
        summarize_feedback (bool): Whether to summarize feedback from multiple providers.

    Returns:
        Dict[str, Any]: Aggregated grading results.
    """
    all_grades = []
    all_feedback = []
    total_max_points = sum(criteria['max_points'] for criteria in rubric.values())

    for llm in llms:
        repeats = num_repeats if repeat_each_provider else 1
        for _ in range(repeats):
            prompt = generate_prompt(rubric, submission)
            response = llm.get_response(prompt)

            logging.debug(f"Response type: {type(response)}")
            logging.debug(f"Response content: {response}")

            result = parse_response(response)
            grade = result['grade']
            feedback = result['feedback']

            if aggregation_method == "bias_adjusted" and bias_adjustments:
                provider_info = llm.get_model_info()
                provider_name = provider_info.get("model_name", "")
                grade += bias_adjustments.get(provider_name, 0)

            if grade is not None:
                all_grades.append(grade)
            if feedback:
                all_feedback.append(feedback)

    if aggregation_method == "simple_average" or aggregation_method == "bias_adjusted":
        average_grade = sum(all_grades) / len(all_grades)
    elif aggregation_method == "weighted_average":
        weights = [llm.get_model_info().get('weight', 1.0) for llm in llms for _ in range(num_repeats if repeat_each_provider else 1)]
        weighted_sum = sum(grade * weight for grade, weight in zip(all_grades, weights))
        average_grade = weighted_sum / sum(weights)
    elif aggregation_method == "median":
        average_grade = median(all_grades)
    else:
        raise ValueError(f"Unsupported aggregation method: {aggregation_method}")

    if summarize_feedback:
        best_llm = max(llms, key=lambda llm: llm.get_model_info().get('weight', 1.0))
        summary_feedback = best_llm.generate_text('Summarize this feedback: ' + ' '.join(all_feedback))
    else:
        summary_feedback = ' '.join(all_feedback)

    provider_info = [{'provider': llm.get_model_info().get("model_name"), 'model': llm.get_model_info().get("version")} for llm in llms]

    sentiment_analysis = analyze_sentiment(submission)
    style_analysis = analyze_style(submission)

    return {
        "average_grade": average_grade,
        "out_of": total_max_points,
        "feedback": summary_feedback,
        "providers": provider_info,
        "nlp_stats": {
            "word_count": style_analysis['word_count'],
            "readability": style_analysis['readability'],
            "sentiment": sentiment_analysis
        }
    }
