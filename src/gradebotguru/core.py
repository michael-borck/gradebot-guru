import logging
import os
from typing import Any

from gradebotguru.grader import grade_submission
from gradebotguru.llm_interface.base_llm import BaseLLM
from gradebotguru.rubric_loader import load_rubric
from gradebotguru.submission_loader import load_submission


def load_and_grade_submissions(
    submissions_path: str, rubric_path: str, llm_interface: BaseLLM
) -> None:
    """
    Load and grade submissions from a directory.

    Parameters:
    - submissions_path (str): The path to the submissions folder.
    - rubric_path (str): The path to the grading rubric.
    - llm_interface (BaseLLM): The LLM interface to generate responses.

    Returns:
    - None

    Examples:
    >>> import tempfile
    >>> from gradebotguru.llm_interface.base_llm import BaseLLM
    >>> class MockLLM(BaseLLM):
    ...     def get_response(self, prompt: str) -> str:
    ...         return "Grade: 85\\nFeedback: Good job!"
    ...     def generate_text(self, prompt: str, **kwargs: Dict[str, Any]) -> str:
    ...         return "Mocked text"
    ...     def get_model_info(self) -> Dict[str, Any]:
    ...         return {"model_name": "mock-model"}
    >>> with tempfile.TemporaryDirectory() as temp_dir:
    ...     rubric_path = os.path.join(temp_dir, "rubric.json")
    ...     with open(rubric_path, "w") as f:
    ...         f.write('{"Content": {"description": "Quality and relevance of content.", "max_points": 10}, "Clarity": {"description": "Clarity of expression and organization.", "max_points": 5}, "Grammar": {"description": "Proper use of grammar and syntax.", "max_points": 5}}')
    ...     submission_path = os.path.join(temp_dir, "submission.txt")
    ...     with open(submission_path, "w") as f:
    ...         f.write("This is the content of submission.")
    ...     load_and_grade_submissions(temp_dir, rubric_path, MockLLM())
    Submission ID: submission.txt
    Grade: 85.0
    Feedback:
    Good job!
    ----------------------------------------
    """
    rubric: dict[str, dict[str, Any]] = load_rubric(rubric_path)

    for filename in os.listdir(submissions_path):
        file_path = os.path.join(submissions_path, filename)
        if os.path.isfile(file_path):
            try:
                submission_text = load_submission(file_path)
                result = grade_submission(
                    submission_id=filename,
                    submission=submission_text,
                    rubric=rubric,
                    llms=[llm_interface],
                    num_repeats=1,
                    repeat_each_provider=False,
                    aggregation_method="simple_average"
                )
                output_results(filename, result["grade"], result["aggregated_response"])
            except ValueError as e:
                logging.warning(f"Skipping unsupported file: {filename} - {e}")


def output_results(submission_id: str, grade: float, feedback: dict[str, Any]) -> None:
    """
    Output the grading results.

    Parameters:
    - submission_id (str): The identifier of the submission.
    - grade (float): The grade for the submission.
    - feedback (str): The feedback for the submission.

    Examples:
    >>> output_results("submission1.txt", 85.0, "Good job!")
    Submission ID: submission1.txt
    Grade: 85.0
    Feedback:
    Good job!
    ----------------------------------------
    """
    print(f"Submission ID: {submission_id}")
    print(f"Grade: {grade}")
    print("Feedback:")
    print(feedback)
    print("-" * 40)
