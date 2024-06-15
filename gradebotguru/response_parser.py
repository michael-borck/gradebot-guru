import re
from typing import Dict, Any


def parse_response(response: str) -> Dict[str, Any]:
    """
    Parse the response from the LLM to extract grades and feedback.

    Parameters:
    - response (str): The response string from the LLM.

    Returns:
    - Dict[str, Any]: A dictionary containing the extracted grades and feedback.
    """
    grade_pattern = re.compile(r"Grade:\s*(\d+(\.\d+)?)")
    feedback_pattern = re.compile(r"Feedback:\s*(.+)", re.DOTALL)

    grade_match = grade_pattern.search(response)
    feedback_match = feedback_pattern.search(response)

    grade = float(grade_match.group(1)) if grade_match else None
    feedback = feedback_match.group(1).strip() if feedback_match else None

    return {
        "grade": grade,
        "feedback": feedback
    }
