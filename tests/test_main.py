import pytest
from pytest_mock import MockerFixture
import sys
import os
from gradebotguru.main import main
from tests.test_utils import MockLLM
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
    Integration test for the main function of the CLI application.

    This test uses mocking to simulate the configuration loading, LLM initialization,
    rubric loading, and submission loading.
    """
    # Mock the command-line arguments
    mocker.patch.object(sys, 'argv', ['main.py', '--config', 'path/to/config.json', '--submissions', 'path/to/submissions'])

    # Mock the load_config function
    mocker.patch('gradebotguru.main.load_config', return_value=mock_config)

    # Mock the create_llm function
    mocker.patch('gradebotguru.main.create_llm', return_value=MockLLM())

    # Mock the load_rubric function
    mocker.patch('gradebotguru.core.load_rubric', return_value=mock_rubric)

    # Mock the load_submission function
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

    # Run the main function
    main()

    # Check that the outputs are as expected
    assert outputs == [
        ('submission1.txt', 85.0, 'Good job!'),
        ('submission2.txt', 85.0, 'Good job!')
    ]
