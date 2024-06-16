import pytest
from pytest_mock import MockerFixture
from gradebotguru.core import load_and_grade_submissions
from gradebotguru.llm_interface.base_llm import BaseLLM
import os
from typing import Any, Dict


class MockLLM(BaseLLM):
    def get_response(self, prompt: str) -> str:
        return "Grade: 85\nFeedback: Good job!"

    def generate_text(self, prompt: str, **kwargs: Dict[str, Any]) -> str:
        return "Mocked text"

    def get_model_info(self) -> Dict[str, Any]:
        return {"model_name": "mock-model"}


def test_load_and_grade_submissions(mocker: MockerFixture) -> None:
    """
    Test the load_and_grade_submissions function.

    This test uses mocking to simulate loading rubric, submissions, and capturing the outputs.
    """
    # Mock the load_rubric function
    mock_rubric = {
        "Content": {"description": "Quality and relevance of content.", "max_points": 10},
        "Clarity": {"description": "Clarity of expression and organization.", "max_points": 5},
        "Grammar": {"description": "Proper use of grammar and syntax.", "max_points": 5}
    }
    mocker.patch('gradebotguru.core.load_rubric', return_value=mock_rubric)

    # Mock the load_submission function
    mock_submissions = {
        'submission1.txt': 'This is the content of submission 1.',
        'submission2.txt': 'This is the content of submission 2.'
    }
    def mock_load_submission(file_path: str) -> str:
        return mock_submissions[os.path.basename(file_path)]
    mocker.patch('gradebotguru.core.load_submission', side_effect=mock_load_submission)

    # Mock the output_results function to capture the outputs
    outputs = []
    def mock_output_results(submission_id: str, grade: float, feedback: str) -> None:
        outputs.append((submission_id, grade, feedback))
    mocker.patch('gradebotguru.core.output_results', side_effect=mock_output_results)

    # Mock os.listdir and os.path.isfile
    mocker.patch('os.listdir', return_value=list(mock_submissions.keys()))
    mocker.patch('os.path.isfile', return_value=True)

    # Run the load_and_grade_submissions function
    load_and_grade_submissions('mock/submissions', 'mock/rubric', MockLLM())

    # Check that the outputs are as expected
    assert outputs == [
        ('submission1.txt', 85.0, 'Good job!'),
        ('submission2.txt', 85.0, 'Good job!')
    ]
