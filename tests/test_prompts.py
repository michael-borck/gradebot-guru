import pytest
from gradebotguru.prompts import generate_prompt, generate_system_prompt, generate_user_prompt
from typing import Dict, Any


@pytest.fixture
def rubric() -> Dict[str, Dict[str, Any]]:
    """
    Fixture to provide a sample grading rubric.

    Returns:
        Dict[str, Dict[str, Any]]: A dictionary representing the grading rubric.
    """
    return {
        "Content": {
            "description": "Quality and relevance of content.",
            "max_points": 10
        },
        "Clarity": {
            "description": "Clarity of expression and organization.",
            "max_points": 5
        },
        "Grammar": {
            "description": "Proper use of grammar and syntax.",
            "max_points": 5
        }
    }


@pytest.fixture
def submission() -> str:
    """
    Fixture to provide a sample student submission.

    Returns:
        str: A sample student submission text.
    """
    return "This is a sample student submission for testing purposes."


def test_generate_system_prompt() -> None:
    """
    Test the generation of the system prompt.

    This test verifies that the system prompt is correctly generated.
    """
    expected_prompt = "You are an AI assistant designed to evaluate student submissions based on a provided rubric."
    actual_prompt = generate_system_prompt()
    assert actual_prompt == expected_prompt


def test_generate_user_prompt(rubric: Dict[str, Dict[str, Any]], submission: str) -> None:
    """
    Test the generation of the user prompt for essay assessment.

    This test verifies that the user prompt is correctly generated for essay-type assessments
    based on the provided rubric and submission.
    """
    expected_prompt = (
        "Assessment Type: Essay\n\n"
        "Using the following rubric:\n\n"
        "- Content: Quality and relevance of content. (Max Points: 10)\n"
        "- Clarity: Clarity of expression and organization. (Max Points: 5)\n"
        "- Grammar: Proper use of grammar and syntax. (Max Points: 5)\n"
        "\nEvaluate the following submission:\n\n"
        "This is a sample student submission for testing purposes.\n\n"
        "Provide detailed feedback and a grade in the following format:\n"
        "Grade: <grade>\n"
        "Feedback: <feedback>\n"
    )
    actual_prompt = generate_user_prompt(rubric, submission, "essay")
    assert actual_prompt == expected_prompt


def test_generate_prompt(rubric: Dict[str, Dict[str, Any]], submission: str) -> None:
    """
    Test the generation of the full prompt for essay assessment.

    This test verifies that the full prompt, including both system and user prompts,
    is correctly generated for essay-type assessments based on the provided rubric and submission.
    """
    expected_prompt = (
        "You are an AI assistant designed to evaluate student submissions based on a provided rubric.\n\n"
        "Assessment Type: Essay\n\n"
        "Using the following rubric:\n\n"
        "- Content: Quality and relevance of content. (Max Points: 10)\n"
        "- Clarity: Clarity of expression and organization. (Max Points: 5)\n"
        "- Grammar: Proper use of grammar and syntax. (Max Points: 5)\n"
        "\nEvaluate the following submission:\n\n"
        "This is a sample student submission for testing purposes.\n\n"
        "Provide detailed feedback and a grade in the following format:\n"
        "Grade: <grade>\n"
        "Feedback: <feedback>\n"
    )
    actual_prompt = generate_prompt(rubric, submission, "essay")
    assert actual_prompt == expected_prompt


def test_generate_user_prompt_with_code(rubric: Dict[str, Dict[str, Any]], submission: str) -> None:
    """
    Test the generation of the user prompt for code assessment.

    This test verifies that the user prompt is correctly generated for code-type assessments
    based on the provided rubric and submission.
    """
    expected_prompt = (
        "Assessment Type: Code\n\n"
        "Using the following rubric:\n\n"
        "- Content: Quality and relevance of content. (Max Points: 10)\n"
        "- Clarity: Clarity of expression and organization. (Max Points: 5)\n"
        "- Grammar: Proper use of grammar and syntax. (Max Points: 5)\n"
        "\nEvaluate the following submission:\n\n"
        "This is a sample student submission for testing purposes.\n\n"
        "Provide detailed feedback and a grade in the following format:\n"
        "Grade: <grade>\n"
        "Feedback: <feedback>\n"
    )
    actual_prompt = generate_user_prompt(rubric, submission, "code")
    assert actual_prompt == expected_prompt


def test_generate_prompt_with_code(rubric: Dict[str, Dict[str, Any]], submission: str) -> None:
    """
    Test the generation of the full prompt for code assessment.

    This test verifies that the full prompt, including both system and user prompts,
    is correctly generated for code-type assessments based on the provided rubric and submission.
    """
    expected_prompt = (
        "You are an AI assistant designed to evaluate student submissions based on a provided rubric.\n\n"
        "Assessment Type: Code\n\n"
        "Using the following rubric:\n\n"
        "- Content: Quality and relevance of content. (Max Points: 10)\n"
        "- Clarity: Clarity of expression and organization. (Max Points: 5)\n"
        "- Grammar: Proper use of grammar and syntax. (Max Points: 5)\n"
        "\nEvaluate the following submission:\n\n"
        "This is a sample student submission for testing purposes.\n\n"
        "Provide detailed feedback and a grade in the following format:\n"
        "Grade: <grade>\n"
        "Feedback: <feedback>\n"
    )
    actual_prompt = generate_prompt(rubric, submission, "code")
    assert actual_prompt == expected_prompt
