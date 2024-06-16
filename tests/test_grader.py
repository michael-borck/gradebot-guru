import pytest
from gradebotguru.grader import grade_submission
from gradebotguru.llm_interface.base_llm import BaseLLM
from tests.test_utils import MockLLM
from typing import Dict, Any


def test_grade_submission() -> None:
    """
    Test the grade_submission function.

    This test verifies that the grade_submission function processes a submission correctly
    and returns the expected grade and feedback.
    """
    rubric: Dict[str, Dict[str, Any]] = {
        "Content": {"description": "Quality and relevance of content.", "max_points": 10},
        "Clarity": {"description": "Clarity of expression and organization.", "max_points": 5},
        "Grammar": {"description": "Proper use of grammar and syntax.", "max_points": 5}
    }
    submission: str = "This is a sample student submission."

    grade, feedback = grade_submission(submission, rubric, MockLLM())

    assert grade == 85.0
    assert feedback == "Good job!"
