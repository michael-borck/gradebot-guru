# tests/test_utils.py
from typing import Any

from gradebotguru.llm_interface.base_llm import BaseLLM


class MockLLM(BaseLLM):
    """
    A mock implementation of the BaseLLM class for testing purposes.

    This class simulates the behavior of an LLM for testing without making actual API calls.
    """

    def get_response(self, prompt: str) -> str:
        """
        Simulate getting a response from the LLM.

        Args:
            prompt (str): The input prompt for the LLM.

        Returns:
            str: A mock response containing a grade and feedback.
        """
        return "Grade: 85\nFeedback: Good job!"

    def generate_text(self, prompt: str, **kwargs: dict[str, Any]) -> str:
        """
        Simulate generating text based on the provided prompt.

        Args:
            prompt (str): The input prompt for the LLM.
            kwargs (Dict[str, Any]): Additional parameters for text generation.

        Returns:
            str: A mock response to the prompt.
        """
        return f"Mock response to prompt: {prompt}"

    def get_model_info(self) -> dict[str, Any]:
        """
        Get mock model information.

        Returns:
            Dict[str, Any]: A dictionary containing mock model information.
        """
        return {"model_name": "mock-model", "version": "1.0"}
