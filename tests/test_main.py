import pytest
from pytest_mock import MockerFixture
from gradebotguru.main import main
import sys
import os
from typing import Any, Dict


@pytest.fixture
def mock_config() -> Dict[str, Any]:
    return {
        'llm_provider': 'mock_provider',
        'api_key': 'mock_api_key',
        'rubric_path': 'path/to/rubric.json'
    }


@pytest.fixture
def mock_rubric() -> Dict[str, Dict[str, Any]]:
    return {
        "Content": {"description": "Quality and relevance of content.", "max_points": 10},
        "Clarity": {"description": "Clarity of expression and organization.", "max_points": 5},
        "Grammar": {"description": "Proper use of grammar and syntax.", "max_points": 5}
    }


@pytest.fixture
def mock_submissions() -> Dict[str, str]:
    return {
        'submission1.txt': 'This is the content of submission 1.',
        'submission2.txt': 'This is the content of submission 2.'
    }


def test_main(mocker: MockerFixture, mock_config: Dict[str, Any], mock_rubric: Dict[str, Dict[str, Any]], mock_submissions: Dict[str, str]) -> None:
    """
    Test the main function of the CLI application.

    This test uses mocking to simulate the configuration loading, LLM initialization,
    rubric loading, and submission loading.
    """
    # Mock the command-line arguments
    mocker.patch.object(sys, 'argv', ['main.py', '--config', 'path/to/config.json', '--submissions', 'path/to/submissions'])

    # Mock the load_config function
    mocker.patch('gradebotguru.main.load_config', return_value=mock_config)

    # Mock the create_llm function
    class MockLLM:
        def get_response(self, prompt: str) -> str:
            return "Grade: 85\nFeedback: Good job!"
    mocker.patch('gradebotguru.main.create_llm', return_value=MockLLM())

    # Mock the load_rubric function
    mocker.patch('gradebotguru.main.load_rubric', return_value=mock_rubric)

    # Mock the load_submissions function
    mocker.patch('gradebotguru.main.load_submissions', return_value=mock_submissions)

    # Mock the output_results function to capture the outputs
    outputs = []

    def mock_output_results(submission_id: str, grade: float, feedback: str) -> None:
        outputs.append((submission_id, grade, feedback))
    mocker.patch('gradebotguru.main.output_results', side_effect=mock_output_results)

    # Run the main function
    main()

    # Check that the outputs are as expected
    assert outputs == [
        ('submission1.txt', 85.0, 'Good job!'),
        ('submission2.txt', 85.0, 'Good job!')
    ]
