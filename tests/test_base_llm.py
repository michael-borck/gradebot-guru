import pytest
from gradebotguru.llm_interface.base_llm import BaseLLM
from typing import Any, Dict


class MockLLM(BaseLLM):
    """
    A mock implementation of the BaseLLM class for testing purposes.
    """

    def get_response(self, prompt: str) -> str:
        """
        Generate a mock response to the given prompt.

        Args:
            prompt (str): The input prompt for the LLM.

        Returns:
            str: A mock response to the prompt.
        """
        return f"Mock response to prompt: {prompt}"

    def generate_text(self, prompt: str, **kwargs: Dict[str, Any]) -> str:
        """
        Generate a mock text response to the given prompt.

        Args:
            prompt (str): The input prompt for the LLM.
            kwargs (Dict[str, Any]): Additional keyword arguments.

        Returns:
            str: A mock response to the prompt.
        """
        return f"Mock response to prompt: {prompt}"

    def get_model_info(self) -> Dict[str, Any]:
        """
        Get mock model information.

        Returns:
            Dict[str, Any]: A dictionary containing mock model information.
        """
        return {"model_name": "MockLLM", "version": "1.0"}


def test_get_response() -> None:
    """
    Test the get_response method of MockLLM.

    This test verifies that the get_response method returns the expected
    mock response for a given prompt.
    """
    llm = MockLLM()
    response = llm.get_response("Hello, world!")
    assert response == "Mock response to prompt: Hello, world!"


def test_generate_text() -> None:
    """
    Test the generate_text method of MockLLM.

    This test verifies that the generate_text method returns the expected
    mock response for a given prompt.
    """
    llm = MockLLM()
    response = llm.generate_text("Hello, world!")
    assert response == "Mock response to prompt: Hello, world!"


def test_get_model_info() -> None:
    """
    Test the get_model_info method of MockLLM.

    This test verifies that the get_model_info method returns the expected
    mock model information.
    """
    llm = MockLLM()
    info = llm.get_model_info()
    assert info == {"model_name": "MockLLM", "version": "1.0"}
