from typing import Dict


def generate_system_prompt() -> str:
    """
    Generate a system prompt to guide the LLM's behavior.

    Returns:
    - str: A system prompt.
    """
    return "You are an AI assistant designed to evaluate student submissions based on a provided rubric."


def generate_user_prompt(rubric: Dict[str, Dict[str, str]], submission: str, assessment_type: str = "essay") -> str:
    """
    Generate a well-formatted prompt for the LLM based on the rubric, submission, and assessment type.

    Parameters:
    - rubric (dict): A dictionary representing the grading rubric.
    - submission (str): The student submission text.
    - assessment_type (str): The type of assessment (e.g., 'essay', 'code').

    Returns:
    - str: A formatted prompt for the LLM.
    """
    prompt = f"Assessment Type: {assessment_type.capitalize()}\n\nUsing the following rubric:\n\n"

    for criterion, details in rubric.items():
        prompt += f"- {criterion}: {details['description']} (Max Points: {details['max_points']})\n"

    prompt += f"\nEvaluate the following submission:\n\n{submission}\n\nProvide detailed feedback and a grade."
    return prompt


def generate_prompt(rubric: Dict[str, Dict[str, str]], submission: str, assessment_type: str = "essay") -> str:
    """
    Generate the full prompt including system and user prompts.

    Parameters:
    - rubric (dict): A dictionary representing the grading rubric.
    - submission (str): The student submission text.
    - assessment_type (str): The type of assessment (e.g., 'essay', 'code').

    Returns:
    - str: The complete prompt for the LLM.
    """
    system_prompt = generate_system_prompt()
    user_prompt = generate_user_prompt(rubric, submission, assessment_type)
    return f"{system_prompt}\n\n{user_prompt}"
