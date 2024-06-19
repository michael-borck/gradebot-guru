import re
from typing import List, Dict, Any, Tuple

def parse_response(text: str) -> Tuple[List[Dict[str, Any]], Dict[str, str]]:
    """
    Parse the response from the LLM to extract criteria and overall feedback.

    Parameters:
    - text (str): The response string from the LLM.

    Returns:
    - Tuple: A tuple containing:
        - List[Dict[str, Any]]: A list of dictionaries for each criterion with keys 'name', 'grade', and 'feedback'.
        - Dict[str, str]: A dictionary with the overall feedback.
    """
    # Define regex patterns for criterion, grade, feedback, and overall sections
    criterion_pattern = re.compile(r'Criterion:\s*(.*)')
    grade_pattern = re.compile(r'Grade:\s*(\d+)')
    feedback_pattern = re.compile(r'Feedback:\s*(.*)', re.DOTALL)
    overall_pattern = re.compile(r'Overall:\s*(.*)', re.DOTALL)

    # Split the text into lines
    original_lines = text.split('\n')
    lines = [line.strip() for line in original_lines]

    criteria = []
    overall = ''
    current_criterion = {}
    collecting_feedback = False
    overall_found = False  # Flag to track if overall has been processed

    for i, line in enumerate(lines):
        criterion_match = criterion_pattern.match(line)
        grade_match = grade_pattern.match(line)
        feedback_match = feedback_pattern.match(line)
        overall_match = overall_pattern.match(line)

        if criterion_match:
            if current_criterion:
                criteria.append(current_criterion)
                current_criterion = {}
            current_criterion['name'] = criterion_match.group(1).strip()
            collecting_feedback = False
        elif grade_match:
            current_criterion['grade'] = int(grade_match.group(1))
            collecting_feedback = False
        elif feedback_match:
            current_criterion['feedback'] = feedback_match.group(1).strip()
            collecting_feedback = True
        elif overall_match and not overall_found:  # Process overall only once
            if current_criterion:
                criteria.append(current_criterion)
                current_criterion = {}
            overall = overall_match.group(1).strip()
            overall_index = i + 1
            for next_line in original_lines[overall_index:]:
                overall += " " + next_line.strip()
            overall_found = True  # Set flag to indicate overall has been processed
            break  # No need to continue after processing overall
        elif collecting_feedback:
            current_criterion['feedback'] += " " + line.strip()

    if current_criterion:
        criteria.append(current_criterion)

    for criterion in criteria:
        if 'grade' not in criterion or not isinstance(criterion['grade'], int):
            criterion['grade'] = 0

    # Save the overall feedback
    overall_feedback = {'overall': overall.strip()}
    
    return criteria, overall_feedback
