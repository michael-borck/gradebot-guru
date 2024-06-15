import pytest
from pytest_mock import MockerFixture
from typing import Any, Dict
from gradebotguru.grader import preprocess_submission, postprocess_results, grade_submission
from gradebotguru.llm_interface.base_llm import BaseLLM


class MockLLM(BaseLLM):
    """
    A mock implementation of the BaseLLM class for testing purposes.
    """

    def get_response(self, prompt: str) -> str:
        """
        Generate a mock response to the given prompt.

        Args:
            prompt (str): The input prompt for the LLM.

        Returns:
            str: A mock response to the prompt.
        """
        return "Grade: 85\nFeedback: Good job!"

    def generate_text(self, prompt: str, **kwargs: Dict[str, Any]) -> str:
        """
        Generate a mock text response to the given prompt.

        Args:
            prompt (str): The input prompt for the LLM.
            kwargs (Dict[str, Any]): Additional keyword arguments.

        Returns:
            str: A mock response to the prompt.
        """
        return f"Mocked text for prompt: {prompt}"

    def get_model_info(self) -> Dict[str, Any]:
        """
        Get mock model information.

        Returns:
            Dict[str, Any]: A dictionary containing mock model information.
        """
        return {"model_name": "MockLLM", "version": "1.0"}


def test_preprocess_submission() -> None:
    """
    Test the preprocess_submission function to ensure it returns the submission unchanged.
    """
    submission = "This is a test submission."
    result = preprocess_submission(submission)
    assert result == submission  # Assuming no changes in preprocessing for now


def test_postprocess_results() -> None:
    """
    Test the postprocess_results function to ensure it returns the grade and feedback unchanged.
    """
    grade = 85.0
    feedback = "Good job!"
    postprocessed_grade, postprocessed_feedback = postprocess_results(grade, feedback)
    assert postprocessed_grade == grade
    assert postprocessed_feedback == feedback


def test_grade_submission(mocker: MockerFixture) -> None:
    """
    Test the grade_submission function to ensure it processes the submission correctly and returns the expected grade and feedback.

    This test uses a mock LLM interface.
    """
    submission = "This is a test submission."
    rubric = {
        "Content": {"description": "Quality and relevance of content.", "max_points": 10},
        "Clarity": {"description": "Clarity of expression and organization.", "max_points": 5},
        "Grammar": {"description": "Proper use of grammar and syntax.", "max_points": 5}
    }

    # Mock the generate_prompt function
    mocker.patch('gradebotguru.prompts.generate_prompt', return_value="Mocked prompt")

    # Use a mock LLM interface
    mock_llm = MockLLM()

    # Mock the parse_response function
    mocker.patch('gradebotguru.response_parser.parse_response', return_value={"grade": 85.0, "feedback": "Good job!"})

    grade, feedback = grade_submission(submission, rubric, mock_llm)
    assert grade == 85.0
    assert feedback == "Good job!"
