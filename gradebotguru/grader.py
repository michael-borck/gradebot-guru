import re
from typing import Dict, Any, List
from statistics import median
from gradebotguru.llm_interface.base_llm import BaseLLM
from gradebotguru.prompts import generate_prompt


def parse_response(response: str) -> Dict[str, Any]:
    """
    Parse the response from the LLM to extract grades and feedback.

    Parameters:
    - response (str): The response string from the LLM.

    Returns:
    - Dict[str, Any]: A dictionary containing the extracted grades and feedback.

    Examples:
    >>> response = "Grade: 85.5\\nFeedback: Good work on the assignment. However, there are some areas that need improvement."
    >>> parse_response(response)
    {'grade': 85.5, 'feedback': 'Good work on the assignment. However, there are some areas that need improvement.'}

    >>> response = "Grade: 90\\nFeedback: "
    >>> parse_response(response)
    {'grade': 90.0, 'feedback': ''}

    >>> response = "Feedback: Excellent effort, but there are a few mistakes."
    >>> parse_response(response)
    {'grade': None, 'feedback': 'Excellent effort, but there are a few mistakes.'}

    >>> response = "No relevant information here."
    >>> parse_response(response)
    {'grade': None, 'feedback': None}
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
    summarize_feedback: bool = True
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
        summarize_feedback (bool): Whether to summarize the feedback from multiple responses.

    Returns:
        Dict[str, Any]: Aggregated grading results.

    Examples:
        >>> class MockLLM(BaseLLM):
        ...     def get_response(self, prompt: str) -> str:
        ...         return "Grade: 85\\nFeedback: Good job!"
        ...     def generate_text(self, prompt: str, **kwargs: Dict[str, Any]) -> str:
        ...         return "Mock response to prompt: " + prompt
        ...     def get_model_info(self) -> Dict[str, Any]:
        ...         return {"model_name": "mock-model", "version": "1.0"}
        >>> llm = MockLLM()
        >>> rubric = {
        ...     "Content": {"description": "Quality and relevance of content.", "max_points": 10},
        ...     "Clarity": {"description": "Clarity of expression and organization.", "max_points": 5},
        ...     "Grammar": {"description": "Proper use of grammar and syntax.", "max_points": 5}
        ... }
        >>> submission = "This is a sample student submission for testing purposes."
        >>> result = grade_submission(submission, rubric, [llm], num_repeats=3, repeat_each_provider=True, aggregation_method="simple_average")
        >>> result['average_grade']
        85.0
        >>> "Good job!" in result['feedback']
        True
        >>> result = grade_submission(submission, rubric, [llm], num_repeats=3, repeat_each_provider=True, aggregation_method="simple_average", summarize_feedback=True)
        >>> result['average_grade']
        85.0
    """
    all_grades = []
    all_feedback = []

    for llm in llms:
        repeats = num_repeats if repeat_each_provider else 1
        for _ in range(repeats):
            prompt = generate_prompt(rubric, submission)
            response = llm.get_response(prompt)
            result = parse_response(response)
            grade = result['grade']
            feedback = result['feedback']

            if grade is not None:
                if aggregation_method == "bias_adjusted" and bias_adjustments:
                    provider_info = llm.get_model_info()
                    provider_name = provider_info.get("model_name", "")
                    grade += bias_adjustments.get(provider_name, 0)
                all_grades.append(grade)

            all_feedback.append(feedback)

    # Aggregate grades
    if aggregation_method == "simple_average":
        average_grade = sum(all_grades) / len(all_grades) if all_grades else None
    elif aggregation_method == "weighted_average":
        weights = [llm.get_model_info().get('weight', 1.0) for llm in llms for _ in range(num_repeats if repeat_each_provider else 1)]
        weighted_sum = sum(grade * weight for grade, weight in zip(all_grades, weights))
        average_grade = weighted_sum / sum(weights) if weights else None
    elif aggregation_method == "median":
        average_grade = median(all_grades) if all_grades else None
    elif aggregation_method == "bias_adjusted":
        average_grade = sum(all_grades) / len(all_grades) if all_grades else None
    else:
        raise ValueError(f"Unsupported aggregation method: {aggregation_method}")

    # Summarize feedback
    if summarize_feedback:
        best_llm = max(llms, key=lambda llm: llm.get_model_info().get('weight', 1.0))
        summary_prompt = f"Summarize the following feedback into a single paragraph: {' '.join(all_feedback)}"
        summarized_feedback = best_llm.get_response(summary_prompt)
        feedback = summarized_feedback
    else:
        feedback = ' '.join(all_feedback)

    return {
        "average_grade": average_grade,
        "feedback": feedback
    }
