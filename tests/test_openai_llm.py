import pytest
from pytest_mock import MockerFixture
from gradebotguru.llm_interface.openai_llm import OpenAILLM
from typing import Any, Dict


@pytest.fixture
def mock_openai(mocker: MockerFixture) -> None:
    """
    Fixture to mock the OpenAI Completion.create method.

    This fixture uses the `mocker` fixture from `pytest_mock` to mock the
    `openai.Completion.create` method, returning a predefined response.

    Args:
        mocker (MockerFixture): The mocker fixture provided by `pytest_mock`.

    Returns:
        None
    """
    mocker.patch("openai.Completion.create", return_value={
        "choices": [{"text": "Mock response"}]
    })


def test_generate_text(mock_openai: None) -> None:
    """
    Test the generate_text method of OpenAILLM.

    This test verifies that the `generate_text` method of the `OpenAILLM` class
    returns the expected mock response when the OpenAI API is mocked.

    Args:
        mock_openai (None): The fixture to mock the OpenAI API.

    Raises:
        AssertionError: If the response from `generate_text` does not match the expected value.
    """
    llm = OpenAILLM(api_key="test_key")
    response = llm.generate_text("Hello, world!")
    assert response == "Mock response"


def test_get_model_info() -> None:
    """
    Test the get_model_info method of OpenAILLM.

    This test verifies that the `get_model_info` method of the `OpenAILLM` class
    returns the expected model information.

    Raises:
        AssertionError: If the returned model information does not match the expected value.
    """
    llm = OpenAILLM(api_key="test_key")
    info = llm.get_model_info()
    assert info == {"model_name": "text-davinci-003", "api_key": "****"}
