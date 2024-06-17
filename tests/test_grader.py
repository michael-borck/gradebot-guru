import pytest
from typing import Dict, Any
from gradebotguru.grader import grade_submission
from tests.test_utils import MockLLM


@pytest.fixture
def mock_rubric() -> Dict[str, Dict[str, Any]]:
    """
    Fixture for a mock rubric.

    Returns:
        Dict[str, Dict[str, Any]]: A dictionary representing the grading rubric.
    """
    return {
        "Content": {"description": "Quality and relevance of content.", "max_points": 10},
        "Clarity": {"description": "Clarity of expression and organization.", "max_points": 5},
        "Grammar": {"description": "Proper use of grammar and syntax.", "max_points": 5}
    }


@pytest.fixture
def mock_submission() -> str:
    """
    Fixture for a mock submission.

    Returns:
        str: A string representing the student submission.
    """
    return "This is a sample student submission for testing purposes."


def test_grade_submission(mock_rubric, mock_submission):
    """
    Test grading a submission with a single LLM provider and multiple repeats.

    Args:
        mock_rubric (Dict[str, Dict[str, Any]]): Mock rubric fixture.
        mock_submission (str): Mock submission fixture.
    """
    llms = [MockLLM()]
    result = grade_submission(mock_submission, mock_rubric, llms, num_repeats=3, repeat_each_provider=True, aggregation_method="simple_average")
    assert result['average_grade'] == 85.0
    assert "Good job!" in result['feedback']


def test_grade_submission_multiple_llms(mock_rubric, mock_submission):
    """
    Test grading a submission with multiple LLM providers and no repeats.

    Args:
        mock_rubric (Dict[str, Dict[str, Any]]): Mock rubric fixture.
        mock_submission (str): Mock submission fixture.
    """
    llms = [MockLLM(), MockLLM()]
    result = grade_submission(mock_submission, mock_rubric, llms, num_repeats=2, repeat_each_provider=False, aggregation_method="simple_average")
    assert result['average_grade'] == 85.0
    assert "Good job!" in result['feedback']


def test_grade_submission_weighted_average(mock_rubric, mock_submission):
    """
    Test grading a submission with multiple LLM providers and weighted average aggregation.

    Args:
        mock_rubric (Dict[str, Dict[str, Any]]): Mock rubric fixture.
        mock_submission (str): Mock submission fixture.
    """
    llms = [MockLLM(), MockLLM()]
    result = grade_submission(mock_submission, mock_rubric, llms, num_repeats=2, repeat_each_provider=False, aggregation_method="weighted_average")
    assert result['average_grade'] == 85.0
    assert "Good job!" in result['feedback']


def test_grade_submission_bias_adjusted(mock_rubric, mock_submission):
    """
    Test grading a submission with multiple LLM providers and bias-adjusted aggregation.

    Args:
        mock_rubric (Dict[str, Dict[str, Any]]): Mock rubric fixture.
        mock_submission (str): Mock submission fixture.
    """
    llms = [MockLLM(), MockLLM()]
    bias_adjustments = {"mock-model": 5.0}
    result = grade_submission(mock_submission, mock_rubric, llms, num_repeats=2, repeat_each_provider=False, aggregation_method="bias_adjusted", bias_adjustments=bias_adjustments)
    assert result['average_grade'] == 85.0
    assert "Good job!" in result['feedback']
