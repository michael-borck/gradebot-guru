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


def generate_user_prompt(rubric: Dict[str, Dict[str, Any]], submission: str, assessment_type: str = "essay") -> str:
    """
    Generate a well-formatted prompt for the LLM based on the rubric, submission, and assessment type.

    Parameters:
    - rubric (Dict[str, Dict[str, Any]]): A dictionary representing the grading rubric.
    - submission (str): The student submission text.
    - assessment_type (str): The type of assessment (e.g., 'essay', 'code').

    Returns:
    - str: A formatted prompt for the LLM.

    >>> rubric = {
    ...     "Content": {"description": "Quality and relevance of content.", "max_points": 10},
    ...     "Clarity": {"description": "Clarity of expression and organization.", "max_points": 5},
    ...     "Grammar": {"description": "Proper use of grammar and syntax.", "max_points": 5}
    ... }
    >>> submission = "This is a sample student submission for testing purposes."
    >>> print(generate_user_prompt(rubric, submission, "essay"))
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
    Provide detailed feedback and a grade in the following format:
    Grade: <grade>
    Feedback: <feedback>
    <BLANKLINE>
    """
    prompt = f"Assessment Type: {assessment_type.capitalize()}\n\nUsing the following rubric:\n\n"

    for criterion, details in rubric.items():
        prompt += f"- {criterion}: {details['description']} (Max Points: {details['max_points']})\n"

    prompt += f"\nEvaluate the following submission:\n\n{submission}\n\nProvide detailed feedback and a grade in the following format:\n"
    prompt += "Grade: <grade>\nFeedback: <feedback>\n"
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
    Provide detailed feedback and a grade in the following format:
    Grade: <grade>
    Feedback: <feedback>
    <BLANKLINE>
    """
    system_prompt = generate_system_prompt()
    user_prompt = generate_user_prompt(rubric, submission, assessment_type)
    return f"{system_prompt}\n\n{user_prompt}"
