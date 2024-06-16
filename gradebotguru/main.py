import argparse
import logging
from typing import Any, Dict
from gradebotguru.logging_config import setup_logging
from gradebotguru.config import load_config
from gradebotguru.llm_interface.factory import create_llm
from gradebotguru.rubric_loader import load_rubric
from gradebotguru.submission_loader import load_submissions
from gradebotguru.grader import grade_submission


def main() -> None:
    """
    Main entry point for the GradeBotGuru CLI application.

    This function parses command-line arguments, loads configurations,
    initializes the LLM interface, loads the rubric, loads submissions,
    grades each submission, and outputs the results.
    """
    # Initialize logging
    setup_logging()

    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="GradeBotGuru CLI")
    parser.add_argument('--config', type=str, help='Path to the configuration file', required=True)
    parser.add_argument('--submissions', type=str, help='Path to the submissions folder', required=True)
    args = parser.parse_args()

    # Load configuration
    config: Dict[str, Any] = load_config(args.config)
    logging.info("Configuration loaded successfully.")

    # Initialize LLM interface
    llm_interface = create_llm(config['llm_provider'], config['api_key'])
    logging.info("LLM interface initialized successfully.")

    # Load rubric
    rubric: Dict[str, Dict[str, Any]] = load_rubric(config['rubric_path'])
    logging.info("Grading rubric loaded successfully.")

    # Load submissions
    submissions: Dict[str, str] = load_submissions(args.submissions)
    logging.info(f"{len(submissions)} submissions loaded successfully.")

    # Grade each submission
    for submission_id, submission_text in submissions.items():
        grade, feedback = grade_submission(submission_text, rubric, llm_interface)
        output_results(submission_id, grade, feedback)


def output_results(submission_id: str, grade: float, feedback: str) -> None:
    """
    Output the grading results.

    Parameters:
    - submission_id (str): The identifier of the submission.
    - grade (float): The grade for the submission.
    - feedback (str): The feedback for the submission.
    """
    print(f"Submission ID: {submission_id}")
    print(f"Grade: {grade}")
    print("Feedback:")
    print(feedback)
    print("-" * 40)


if __name__ == "__main__":
    main()
