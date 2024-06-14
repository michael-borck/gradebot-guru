# Core grading logic
'''
# Core grading logic

class Grader:
    def __init__(self, rubric, submissions):
        # Initialize the Grader with a rubric and student submissions

    def generate_prompts(self):
        # Generate prompts for the LLM based on the rubric and submissions

    def grade(self):
        # Send prompts to the LLM and receive responses
        # Parse responses to extract grades and feedback
        # Return grades and feedback
'''

class Grader:
    def __init__(self, rubric):
        # Initialize with a rubric
        self.rubric = rubric

    def grade(self, submission):
        # 1. Preprocess submission (clean text, extract features, etc.)
        preprocessed_submission = preprocess_submission(submission)

        # 2. Generate LLM prompt (using llm_interface/prompts.py)
        prompt = llm_interface.prompts.generate_grading_prompt(preprocessed_submission, self.rubric)

        # 3. Send prompt to LLM (using llm_interface/api.py)
        response = llm_interface.api.get_response(prompt)

        # 4. Parse LLM response (extract grade, feedback)
        grade, feedback = llm_interface.api.parse_response(response)

        # 5. Postprocess results (optional, adjust grade based on rules)
        postprocessed_grade, postprocessed_feedback = postprocess_results(grade, feedback)

        return postprocessed_grade, postprocessed_feedback
