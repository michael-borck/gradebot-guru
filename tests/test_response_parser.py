import pytest

from gradebotguru.response_parser import parse_response


def test_parse_response_with_valid_data() -> None:
    """
    Test parsing a valid response with grade and feedback.
    """
    response = "Grade: 85.5\nFeedback: Good work on the assignment. However, there are some areas that need improvement."
    expected_result = {
        "grade": 85.5,
        "feedback": "Good work on the assignment. However, there are some areas that need improvement.",
    }
    actual_result = parse_response(response)
    assert actual_result == expected_result


def test_parse_response_without_feedback() -> None:
    """
    Test parsing a response with grade but no feedback.
    """
    response = "Grade: 90\nFeedback: "
    expected_result = {"grade": 90.0, "feedback": ""}
    actual_result = parse_response(response)
    assert actual_result == expected_result


def test_parse_response_without_grade() -> None:
    """
    Test parsing a response with feedback but no grade.
    """
    response = "Feedback: Excellent effort, but there are a few mistakes."
    expected_result = {
        "grade": None,
        "feedback": "Excellent effort, but there are a few mistakes.",
    }
    actual_result = parse_response(response)
    assert actual_result == expected_result


def test_parse_response_with_no_matching_patterns() -> None:
    """
    Test parsing a response with no matching grade or feedback patterns.
    """
    response = "No relevant information here."
    expected_result = {"grade": None, "feedback": None}
    actual_result = parse_response(response)
    assert actual_result == expected_result


def test_parse_response_with_partial_grade() -> None:
    """
    Test parsing a response with a partial grade (no decimal part).
    """
    response = "Grade: 75\nFeedback: Satisfactory performance, but there is room for improvement."
    expected_result = {
        "grade": 75.0,
        "feedback": "Satisfactory performance, but there is room for improvement.",
    }
    actual_result = parse_response(response)
    assert actual_result == expected_result


if __name__ == "__main__":
    pytest.main()
