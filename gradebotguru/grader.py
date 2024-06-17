from typing import List, Dict, Any
from gradebotguru.llm_interface.base_llm import BaseLLM
from gradebotguru.prompts import generate_prompt
from gradebotguru.response_parser import parse_response


def grade_submission(submission: str, rubric: Dict[str, Dict[str, Any]], llms: List[BaseLLM], num_repeats: int, repeat_each_provider: bool) -> Dict[str, Any]:
    """
    Grade a student submission using multiple LLM providers and repeats.

    Args:
        submission (str): The student submission text.
        rubric (Dict[str, Dict[str, Any]]): The grading rubric.
        llms (List[BaseLLM]): List of LLM providers.
        num_repeats (int): Number of times to repeat the grading process.
        repeat_each_provider (bool): Whether to repeat grading for each provider.

    Returns:
        Dict[str, Any]: Aggregated grading results.

    Examples:
        >>> class MockLLM(BaseLLM):
        ...     def generate_text(self, prompt: str, **kwargs: Dict[str, Any]) -> str:
        ...        return "Mock response to prompt: " + prompt
        ...     def get_model_info(self) -> Dict[str, Any]:
        ...         return {"model_name": "mock-model", "version": "1.0"}
        ...     def get_response(self, prompt: str) -> str:
        ...         return "Grade: 85\\nFeedback: Good work!"
        >>> llm = MockLLM()
        >>> rubric = {
        ...     "Content": {"description": "Quality and relevance of content.", "max_points": 10},
        ...     "Clarity": {"description": "Clarity of expression and organization.", "max_points": 5},
        ...     "Grammar": {"description": "Proper use of grammar and syntax.", "max_points": 5}
        ... }
        >>> submission = "This is a sample student submission for testing purposes."
        >>> result = grade_submission(submission, rubric, [llm], num_repeats=3, repeat_each_provider=True)
        >>> result['average_grade']
        85.0
        >>> "Good work!" in result['feedback']
        True
    """
    all_grades = []
    all_feedback = []

    for llm in llms:
        repeats = num_repeats if repeat_each_provider else 1
        for _ in range(repeats):
            prompt = generate_prompt(rubric, submission)
            response = llm.get_response(prompt)
            parsed_response = parse_response(response)
            grade = parsed_response.get("grade")
            feedback = parsed_response.get("feedback")
            all_grades.append(grade)
            all_feedback.append(feedback)

    # Aggregate results
    average_grade = sum(filter(None, all_grades)) / len(all_grades)
    aggregated_feedback = " ".join(filter(None, all_feedback))

    return {
        "average_grade": average_grade,
        "feedback": aggregated_feedback
    }
