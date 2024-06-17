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

    config = load_config(args.config)
    setup_logging(level=config['logging_level'], filename=config.get('log_file'))
    logging.info("Configuration loaded successfully.")

    llm_providers = [create_llm(provider) for provider in config['llm_providers']]
    rubric = load_rubric(config['rubric_path'])
    submissions = load_submissions(args.submissions)

    number_of_repeats = config.get('number_of_repeats', 1)
    repeat_each_provider = config.get('repeat_each_provider', False)
    aggregation_method = config.get('aggregation_method', 'simple_average')
    bias_adjustments = config.get('bias_adjustments', {})
    summarize_feedback = config.get('summarize_feedback', False)

    for submission_id, submission_text in submissions.items():
        result = grade_submission(
            submission_text,
            rubric,
            llm_providers,
            num_repeats=number_of_repeats,
            repeat_each_provider=repeat_each_provider,
            aggregation_method=aggregation_method,
            bias_adjustments=bias_adjustments,
            summarize_feedback=summarize_feedback
        )
        print(f"LLM Details: {result['providers']}")
        print(f"Submission ID: {submission_id}, Average Grade: {result['average_grade']}/{result['out_of']}, {result['nlp_stats']}")
        print(f"Feedback: {result['feedback']}")


if __name__ == "__main__":
    main()
