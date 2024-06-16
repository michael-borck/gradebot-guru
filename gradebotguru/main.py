import argparse
import logging
from gradebotguru.config import load_config
from gradebotguru.rubric_loader import load_rubric
from gradebotguru.submission_loader import load_submissions
from gradebotguru.grader import grade_submission
from gradebotguru.llm_interface.factory import create_llm
from gradebotguru.logging_config import setup_logging


def main():
    parser = argparse.ArgumentParser(description="Grade student submissions using an LLM.")
    parser.add_argument("--config", type=str, required=True, help="Path to the configuration file.")
    parser.add_argument("--submissions", type=str, required=True, help="Path to the submissions directory.")
    args = parser.parse_args()

    setup_logging()
    config = load_config(args.config)
    logging.info("Configuration loaded successfully.")

    llm_interface = create_llm(config)
    rubric = load_rubric(config['rubric_path'])
    submissions = load_submissions(args.submissions)

    for submission_id, submission_text in submissions.items():
        grade, feedback = grade_submission(submission_text, rubric, llm_interface)
        print(f"Submission ID: {submission_id}, Grade: {grade}, Feedback: {feedback}")


if __name__ == "__main__":
    main()
