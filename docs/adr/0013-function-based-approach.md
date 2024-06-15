
# ADR 0013: Adopt Function-Based Design Approach

## Context
GradeBotGuru aims to automate the evaluation of student submissions using an AI-powered grading system. The core tasks involve loading submissions, building prompts, interacting with an LLM (Language Learning Model), parsing responses, and saving grades and feedback.

## Decision
We will adopt a function-based design approach for the following reasons:
1. **Simplicity**: The tasks involved are straightforward and do not require complex state management.
2. **Clarity**: A function-based approach keeps all data and functionality visible within functions, reducing the complexity of understanding the flow.
3. **Personal Preference**: The team has a preference for function-based design, which aligns with the skills and background of the developers.

## Implications
1. **Consistency**: The entire project will follow a function-based design, avoiding the use of OO patterns unless absolutely necessary.
2. **Visibility**: All data and operations will be kept within functions, ensuring that the flow of data and the sequence of operations are clear and explicit.
3. **Maintenance**: The project will be easier to maintain and extend due to the straightforward nature of the function-based code.

## Implementation

### main.py

```python
import argparse
from gradebotguru.logging_config import setup_logging
from gradebotguru.config import load_config
from gradebotguru.llm_inference.factory import create_llm
from gradebotguru.rubric_loader import load_rubric
from gradebotguru.submission_loader import load_submissions
from gradebotguru.grader import grade_submission

def main():
    setup_logging()

    parser = argparse.ArgumentParser(description="GradeBotGuru CLI")
    parser.add_argument('--config', type=str, help='Path to the configuration file', required=True)
    parser.add_argument('--submissions', type=str, help='Path to the submissions folder', required=True)
    args = parser.parse_args()

    config = load_config(args.config)
    llm_interface = create_llm(config['llm_provider'])
    rubric = load_rubric(config['rubric_path'])

    submissions = load_submissions(args.submissions)

    for submission in submissions:
        grade, feedback = grade_submission(submission, rubric)
        print(f"Grade: {grade}, Feedback: {feedback}")

if __name__ == "__main__":
    main()
```

### grader.py

```python
from gradebotguru.prompts import generate_prompt
from gradebotguru.response_parser import parse_response
import llm_interface

def preprocess_submission(submission):
    return submission

def postprocess_results(grade, feedback):
    return grade, feedback

def grade_submission(submission, rubric):
    preprocessed_submission = preprocess_submission(submission)
    prompt = generate_prompt(rubric, preprocessed_submission)
    response = llm_interface.api.get_response(prompt)
    result = parse_response(response)
    postprocessed_grade, postprocessed_feedback = postprocess_results(result['grade'], result['feedback'])
    return postprocessed_grade, postprocessed_feedback
```
