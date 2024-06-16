import argparse
import logging
from typing import Any, Dict
from gradebotguru.logging_config import setup_logging
from gradebotguru.config import load_config
from gradebotguru.llm_interface.factory import create_llm
from gradebotguru.core import load_and_grade_submissions


def main() -> None:
    """
    Main entry point for the GradeBotGuru CLI application.

    This function parses command-line arguments, loads configurations,
    initializes the LLM interface, and processes submissions one at a time.
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

    # Load and grade submissions
    load_and_grade_submissions(args.submissions, config['rubric_path'], llm_interface)

if __name__ == "__main__":
    main()
