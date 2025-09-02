import logging
from typing import Any

from ollama import Client

from gradebotguru.llm_interface.base_llm import BaseLLM


class OllamaLLM(BaseLLM):
    """
    Ollama LLM class for interacting with the Ollama server.

    Args:
        api_key (str): The API key for authentication with the Ollama server.
        server_url (str): The URL of the Ollama server.
        model (str): The model to use for generating responses.

    Attributes:
        api_key (str): The API key for authentication.
        server_url (str): The URL of the Ollama server.
        model (str): The model to use for generating responses.
        client (Client): The custom client for interacting with the Ollama server.
    """

    def __init__(
        self, api_key: str, server_url: str, model: str = "llama3", weight: float = 1.0
    ) -> None:
        self.api_key = api_key
        self.server_url = server_url
        self.model = model
        self.weight = weight
        self.client = Client(host=server_url)

    def generate_text(self, prompt: str, **kwargs: dict[str, Any]) -> str:
        """
        Generate a text response using the Ollama LLM.

        Args:
            prompt (str): The input prompt for the LLM.
            kwargs (Dict[str, Any]): Additional keyword arguments.

        Returns:
            str: The generated text response.
        """
        messages = [{"role": "user", "content": prompt}]
        response = self.client.chat(model=self.model, messages=messages)

        # Handle the response structure properly - Ollama returns a ChatResponse object
        if hasattr(response, "message") and hasattr(response.message, "content"):
            return str(response.message.content)
        else:
            # Fallback for any unexpected response format
            return str(response)

    def get_response(self, prompt: str, **kwargs: dict[str, Any]) -> str:
        """
        Generate a response using the Ollama LLM.

        Args:
            prompt (str): The input prompt for the LLM.

        Returns:
            str: The generated response.
        """
        try:
            response = self.generate_text(prompt, **kwargs)
            logging.debug(f"Response from Ollama: {response}")
            return response
        except Exception as e:
            logging.error(f"Error getting response from Ollama: {e}")
            raise

    def get_model_info(self) -> dict[str, Any]:
        """
        Get information about the Ollama LLM model.

        Returns:
            Dict[str, Any]: A dictionary containing model information.
        """
        return {
            "provider": "Ollama",
            "model_name": self.model,
            "weight": self.weight,
            "server_url": self.server_url,
        }
