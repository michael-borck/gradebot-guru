import argparse
import logging
import pprint

from gradebotguru.config import load_config
from gradebotguru.grader import grade_submission
from gradebotguru.llm_interface.factory import create_llms
from gradebotguru.logging_config import setup_logging
from gradebotguru.rubric_loader import load_rubric
from gradebotguru.submission_loader import load_submissions


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Grade student submissions using an LLM."
    )
    parser.add_argument(
        "--config", type=str, required=True, help="Path to the configuration file."
    )
    parser.add_argument(
        "--submissions",
        type=str,
        required=True,
        help="Path to the submissions directory.",
    )
    args = parser.parse_args()

    setup_logging()
    config = load_config(args.config)
    logging.info("Configuration loaded successfully.")

    llms = create_llms(config)
    rubric = load_rubric(config["rubric_path"])
    submissions = load_submissions(args.submissions)
    logging.info("Submissions loaded successfully.")

    for submission_id, submission_text in submissions.items():
        result = grade_submission(
            submission_id=submission_id,
            submission=submission_text,
            rubric=rubric,
            llms=llms,
            num_repeats=config["number_of_repeats"],
            repeat_each_provider=config["repeat_each_provider"],
            aggregation_method=config["aggregation_method"],
            bias_adjustments=config.get("bias_adjustments", {}),
            prompt_template=config["llm_prompt_template"],
            summarize_feedback=config.get("summarize_feedback", True),
        )

        print(f"{result['grade']}")
        pprint.pprint(result["aggregated_response"])


if __name__ == "__main__":
    main()
