import pytest
from gradebotguru.grader import grade_submission
from tests.test_utils import MockLLM

@pytest.fixture
def mock_rubric():
    return {
        "Content": {"description": "Quality and relevance of content.", "max_points": 10},
        "Clarity": {"description": "Clarity of expression and organization.", "max_points": 5},
        "Grammar": {"description": "Proper use of grammar and syntax.", "max_points": 5}
    }

@pytest.fixture
def mock_submission():
    return "This is a sample student submission for testing purposes."

def test_grade_submission(mock_rubric, mock_submission):
    llms = [MockLLM()]
    result = grade_submission(mock_submission, mock_rubric, llms, num_repeats=3, repeat_each_provider=True)

    assert result['average_grade'] == 85.0
    assert "Good job!" in result['feedback']

def test_grade_submission_multiple_llms(mock_rubric, mock_submission):
    llms = [MockLLM(), MockLLM()]
    result = grade_submission(mock_submission, mock_rubric, llms, num_repeats=2, repeat_each_provider=False)

    assert result['average_grade'] == 85.0
    assert result['feedback'].count("Good job!") == 2
