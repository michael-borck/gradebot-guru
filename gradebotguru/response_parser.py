import re
from typing import Dict, Any


def clean_grades(grades_dict):
    """
    Cleans a dictionary of grades by replacing 'N/A' with 0 and extracting the first number from fraction-like strings.

    Args:
        grades_dict: A dictionary containing grade values (int, float, str).

    Returns:
        A new dictionary with cleaned grade values.
    """

    cleaned_grades = {}
    for course, grade in grades_dict.items():
        if grade == 'N/A':
            cleaned_grades[course] = 0
        elif isinstance(grade, str) and '/' in grade:  # Handle '5/7' like cases
            cleaned_grades[course] = int(grade.split('/')[0]) 
        else:
            cleaned_grades[course] = grade

    return cleaned_grades


def parse_response(response: str) -> Dict[str, Any]:
    """
    Parse the response from the LLM to extract grades and feedback.

    Parameters:
    - response (str): The response string from the LLM.

    Returns:
    - Dict[str, Any]: A dictionary containing the extracted grades, feedback, total score, and max score.

    Examples:
    >>> response = "Criterion: Content\\nGrade: 9/10\\nFeedback: Strong focus on LLMs.\\nTotal Score: 23/25"
    >>> parse_response(response)
    {'grades': {'Content': 9}, 'feedback': {'Content': 'Strong focus on LLMs.'}, 'total_score': 23, 'max_score': 25}

    >>> response = "Criterion: Grammar\\nGrade: 4.5/5\\nFeedback: Minor errors.\\nTotal Score: 23.5/25"
    >>> parse_response(response)
    {'grades': {'Grammar': 4.5}, 'feedback': {'Grammar': 'Minor errors.'}, 'total_score': 23.5, 'max_score': 25}

    >>> response = "Feedback: Excellent effort, but there are a few mistakes."
    >>> parse_response(response)
    {'grades': {}, 'feedback': {'General': 'Excellent effort, but there are a few mistakes.'}, 'total_score': None, 'max_score': None}

    >>> response = "No relevant information here."
    >>> parse_response(response)
    {'grades': {}, 'feedback': {}, 'total_score': None, 'max_score': None}
    """
    grades_pattern = re.compile(r"Criterion:\s*(.+?)\s*Grade:\s*(\d+(?:\.\d+)?)(?:\/\d+)?\s*Feedback:\s*(.+?)(?=\nCriterion:|$)", re.DOTALL)
    overall_feedback_pattern = re.compile(r"Overall:\s*(.+)", re.DOTALL)

    grades_matches = grades_pattern.findall(response)
    overall_feedback_match = overall_feedback_pattern.search(response)

    grades = {}
    feedback = {}
    for match in grades_matches:
        criterion, grade, fb = match
        grades[criterion.strip()] = float(grade)
        feedback[criterion.strip()] = fb.strip()

    if grades:
        grades = clean_grades(grades)
        total_score = sum(grades.values())
    else:
        total_score = 0

    overall_feedback = overall_feedback_match.group(1).strip() if overall_feedback_match else None

    return {
        "breakdown": grades,
        "criterion_feedback": feedback,
        "total_score": total_score,
        "overall_feedback": overall_feedback
    }
