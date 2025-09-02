import os
from tempfile import TemporaryDirectory

from gradebotguru.core import load_and_grade_submissions
from tests.test_utils import MockLLM


def test_end_to_end() -> None:
    """
    Test the entire grading workflow from loading rubrics and submissions to generating prompts,
    interacting with the LLM, and parsing responses.
    """
    mock_rubric_csv = """criterion,description,max_points
    Content,Quality and relevance of content.,10
    Clarity,Clarity of expression and organization.,5
    Grammar,Proper use of grammar and syntax.,5
    """

    mock_submissions = {
        "submission1.txt": "This is the content of submission 1.",
        "submission2.txt": "This is the content of submission 2.",
    }

    with TemporaryDirectory() as temp_dir:
        rubric_path = os.path.join(temp_dir, "rubric.csv")
        with open(rubric_path, "w") as f:
            f.write(mock_rubric_csv)

        for filename, content in mock_submissions.items():
            file_path = os.path.join(temp_dir, filename)
            with open(file_path, "w") as f:
                f.write(content)

        llm_interface = MockLLM()

        outputs = []

        def mock_output_results(
            submission_id: str, grade: float, feedback: str
        ) -> None:
            outputs.append((submission_id, grade, feedback))

        # Patch the output_results function in the core module
        from gradebotguru import core

        core.output_results = mock_output_results

        # Run the end-to-end test
        load_and_grade_submissions(temp_dir, rubric_path, llm_interface)

        # Validate results
        expected_results = [
            ("submission1.txt", 85.0, "Good job!"),
            ("submission2.txt", 85.0, "Good job!"),
        ]
        assert outputs == expected_results
