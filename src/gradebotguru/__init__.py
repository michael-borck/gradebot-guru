"""
GradeBot Guru: AI-powered grading assistant for fast, accurate, and insightful feedback.
"""

from .config import load_config
from .grader import grade_submission
from .llm_interface.factory import create_llms
from .main import main
from .rubric_loader import load_rubric
from .submission_loader import load_submissions

__version__ = "0.6.3"
__author__ = "Michael Borck"
__email__ = "michael@borck.me"

__all__ = [
    "main",
    "grade_submission",
    "load_config",
    "load_rubric",
    "load_submissions",
    "create_llms",
]
