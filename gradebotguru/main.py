'''
Main entry point for the CLI application
- Parse command-line arguments
- Load rubric file using rubric_loader
- Load student submissions using submission_loader
- Initialize grader with loaded rubric and submissions
- Generate and send prompts to the LLM using llm_interface
- Parse responses using response_parser
- Output results to the CLI
'''

from gradebotguru.config import load_config
from gradebotguru.rubric_loader import load_rubric
from gradebotguru.submission_loader import load_submissions
from gradebotguru.grader import Grader
from gradebotguru.llm_interface.factory import create_llm
from gradebotguru.logging_config import setup_logging

def main():
    # Initialize logging
    setup_logging()

    # Load configuration
    config = load_config()

    # Initialize LLM interface
    llm_interface = create_llm(config['llm_provider'])

    # Load rubric
    rubric = load_rubric(config['rubric_path'])

    # Initialize Grader
    grader = Grader(rubric)

    # Load submissions
    submissions = load_submissions('path/to/submissions')

    # Grade each submission
    for submission in submissions:
        grade, feedback = grader.grade(submission)
        print(f"Grade: {grade}, Feedback: {feedback}")

if __name__ == "__main__":
    main()
