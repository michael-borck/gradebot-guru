import re
from typing import Dict, Any

def parse_response(response: str) -> Dict[str, Any]:
    """
    Parse the response from the LLM to extract grades and feedback.

    Parameters:
    - response (str): The response string from the LLM.

    Returns:
    - Dict[str, Any]: A dictionary containing the extracted grades and feedback.

    Examples:
    >>> response = "Grade: 85.5\\nFeedback: Good work on the assignment. However, there are some areas that need improvement."
    >>> parse_response(response)
    {'grade': 85.5, 'feedback': 'Good work on the assignment. However, there are some areas that need improvement.'}

    >>> response = "Grade: 90\\nFeedback: "
    >>> parse_response(response)
    {'grade': 90.0, 'feedback': ''}

    >>> response = "Feedback: Excellent effort, but there are a few mistakes."
    >>> parse_response(response)
    {'grade': None, 'feedback': 'Excellent effort, but there are a few mistakes.'}

    >>> response = "No relevant information here."
    >>> parse_response(response)
    {'grade': None, 'feedback': None}
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

if __name__ == "__main__":
    import doctest
    doctest.testmod()
