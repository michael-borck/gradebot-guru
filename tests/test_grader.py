import pytest
from typing import Dict, Any
from gradebotguru.grader import grade_submission
from tests.test_utils import MockLLM


@pytest.fixture
def mock_rubric() -> Dict[str, Dict[str, Any]]:
    return {
        "Content": {"description": "Quality and relevance of content.", "max_points": 10},
        "Clarity": {"description": "Clarity of expression and organization.", "max_points": 5},
        "Grammar": {"description": "Proper use of grammar and syntax.", "max_points": 5}
    }


@pytest.fixture
def mock_submission() -> str:
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
    assert result['out_of'] == 20
    assert "Good job!" in result['feedback']
    assert 'sentiment' in result['nlp_stats']
    assert 'word_count' in result['nlp_stats']
    assert 'readability' in result['nlp_stats']


def test_grade_submission_multiple_llms(mock_rubric, mock_submission):
    """
    Test grading a submission with multiple LLM providers and no repeats.

    Args:
        mock_rubric (Dict[str, Dict[str, Any]]): Mock rubric fixture.
        mock_submission (str): Mock submission fixture.
    """
    llms = [MockLLM(), MockLLM()]
    result = grade_submission(mock_submission, mock_rubric, llms, num_repeats=2, repeat_each_provider=False, aggregation_method="simple_average", summarize_feedback=False)
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
    result = grade_submission(mock_submission, mock_rubric, llms, num_repeats=2, repeat_each_provider=False, aggregation_method="bias_adjusted", bias_adjustments=bias_adjustments, summarize_feedback=False)
    assert result['average_grade'] == 90.0
    assert "Good job!" in result['feedback']


def test_grade_submission_summarize_feedback(mock_rubric, mock_submission):
    """
    Test grading a submission with feedback summarization enabled.

    Args:
        mock_rubric (Dict[str, Dict[str, Any]]): Mock rubric fixture.
        mock_submission (str): Mock submission fixture.
    """
    llms = [MockLLM()]
    result = grade_submission(mock_submission, mock_rubric, llms, num_repeats=3, repeat_each_provider=True, aggregation_method="simple_average", summarize_feedback=True)
    assert result['average_grade'] == 85.0
    #assert len(result['feedback']) <= sum(len(f) for f in result['feedback'].split('Mock response to prompt: '))
