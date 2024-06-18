from typing import Dict, Any


def generate_system_prompt() -> str:
    """
    Generate a system prompt to guide the LLM's behavior.

    Returns:
    - str: A system prompt.

    >>> generate_system_prompt()
    'You are an AI assistant designed to evaluate student submissions based on a provided rubric.'
    """
    return "You are an AI assistant designed to evaluate student submissions based on a provided rubric."


def generate_user_prompt(rubric: Dict[str, Dict[str, Any]], submission: str, prompt_template: str, assessment_type: str = "essay") -> str:
    """
    Generate a well-formatted prompt for the LLM based on the rubric, submission, and assessment type.

    Parameters:
    - rubric (Dict[str, Dict[str, Any]]): A dictionary representing the grading rubric.
    - submission (str): The student submission text.
    - prompt_template (str): Custom prompt template for LLMs.
    - assessment_type (str): The type of assessment (e.g., 'essay', 'code').

    Returns:
    - str: A formatted prompt for the LLM.

    >>> rubric = {
    ...     "Content": {"description": "Quality and relevance of content.", "max_points": 10},
    ...     "Clarity": {"description": "Clarity of expression and organization.", "max_points": 5},
    ...     "Grammar": {"description": "Proper use of grammar and syntax.", "max_points": 5}
    ... }
    >>> submission = "This is a sample student submission for testing purposes."
    >>> template = "Evaluate the following submission based on the rubric provided. The rubric is as follows: {rubric}. The student submission is as follows: {submission}."
    >>> print(generate_user_prompt(rubric, submission, template, "essay"))
    Evaluate the following submission based on the rubric provided. The rubric is as follows: - Content: Quality and relevance of content. (Max Points: 10) - Clarity: Clarity of expression and organization. (Max Points: 5) - Grammar: Proper use of grammar and syntax. (Max Points: 5). The student submission is as follows: This is a sample student submission for testing purposes.
    """
    rubric_str = ""
    for criterion, details in rubric.items():
        description = details.get('description', '')
        max_points = details['max_points']
        rubric_str += f"- {criterion}: {description} (Max Points: {max_points}) "
    prompt = prompt_template.format(rubric=rubric_str.strip(), submission=submission.strip())
    return prompt


def generate_prompt(rubric: Dict[str, Dict[str, Any]], submission: str, assessment_type: str = "essay") -> str:
    """
    Generate the full prompt including system and user prompts.

    Parameters:
    - rubric (Dict[str, Dict[str, Any]]): A dictionary representing the grading rubric.
    - submission (str): The student submission text.
    - assessment_type (str): The type of assessment (e.g., 'essay', 'code').

    Returns:
    - str: The complete prompt for the LLM.

    >>> rubric = {
    ...     "Content": {"description": "Quality and relevance of content.", "max_points": 10},
    ...     "Clarity": {"description": "Clarity of expression and organization.", "max_points": 5},
    ...     "Grammar": {"description": "Proper use of grammar and syntax.", "max_points": 5}
    ... }
    >>> submission = "This is a sample student submission for testing purposes."
    >>> print(generate_prompt(rubric, submission, "essay"))
    You are an AI assistant designed to evaluate student submissions based on a provided rubric.
    <BLANKLINE>
    Assessment Type: Essay
    <BLANKLINE>
    Using the following rubric:
    <BLANKLINE>
    - Content: Quality and relevance of content. (Max Points: 10)
    - Clarity: Clarity of expression and organization. (Max Points: 5)
    - Grammar: Proper use of grammar and syntax. (Max Points: 5)
    <BLANKLINE>
    Evaluate the following submission:
    <BLANKLINE>
    This is a sample student submission for testing purposes.
    <BLANKLINE>
    Provide detailed feedback and a grade for each criterion in the following format:
    <BLANKLINE>
    Criterion: <criterion_name>
    Grade: <grade>
    Feedback: <feedback>
    <BLANKLINE>
    Provide the total score in the format: Total Score: <total_score>/<max_score>
    """
    system_prompt = generate_system_prompt()
    user_prompt = generate_user_prompt(rubric, submission, assessment_type)
    # user_prompt += "\n\nPlease write as if you are talking directly to the student, so use 'you' instead of 'the student'."
    user_prompt += "\n\nPlease make it feel like you are real person given direct feedback to the student."
    # user_prompt += "\nPlease provide feedback in a constructive and respectful manner."
    # user_prompt += "\nPlease provide feedback that is specific, actionable, and relevant to the submission."
    # user_prompt += "\nPlease provide feedback that is clear, concise, and well-organized."
    # user_prompt += "\nPlease provide feedback that is supportive, encouraging, and motivating."
    # user_prompt += "\nPlease provide feedback that is fair, consistent, and unbiased."
    # user_prompt += "\nPlease provide feedback that is accurate, objective, and evidence-based."   
    # user_prompt += "\nUse proper grammar, punctuation, and spelling in the output"
    # user_prompt += "\nUse complete sentences and paragraphs in the output"
    # user_prompt += "\nUse a respectful and professional tone in the output"
    user_prompt += "\nPlease provide detailed feedback and a grade for each criterion in the following format:\n\n"
    user_prompt += "Criterion: <criterion_name>\nGrade: <grade>\nFeedback: <feedback>\n\n"
    user_prompt += "\nIf the submission is missing a criterion, please provide a 0 for the grade and 'N/A' for feedback for that criterion.\n\n"
    # user_prompt += "Provide the total score in the format: Total Score: <total_score>/<max_score>"
    user_prompt += "\nAt the very end of response provide one paragraph of overall feedback for the submission in the format: Overall: .\n\n"
    user_prompt += "\n Do not include a final grade, overall grade, overall score, final score or total score in the output"
    user_prompt += "Do not include any markdown in the output"
    # user_prompt += "Do not include any identifying information in the output"
    # user_prompt += "Do not include any offensive, inappropriate, or irrelevant content in the output"
    # user_prompt += "Follow the guidelines provided in the rubric and the prompt"
    # user_prompt += "Use the rubric and the submission to guide your evaluation"
    # user_prompt += "Follow these instructions  and do not include any additional information in the output"
    # user_prompt += "Do not make anything up or include any additional information in the output"
    # user_prompt += "Please take you time and think step by step to provide the best feedback"
    return f"{system_prompt}\n\n{user_prompt}"