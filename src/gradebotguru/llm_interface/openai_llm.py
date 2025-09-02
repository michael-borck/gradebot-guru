import logging
from typing import Any

from openai import OpenAI

from gradebotguru.llm_interface.base_llm import BaseLLM


class OpenAILLM(BaseLLM):
    def __init__(
        self,
        api_key: str,
        model: str = "gpt-3.5-turbo-0125",
        temperature: float = 0.7,
        weight: float = 1.0,
    ):
        """
        Initialize the OpenAILLM class with the provided API key and model.

        Args:
            api_key (str): The API key for accessing the OpenAI API.
            model (str): The model to use for generating text. Default is "gpt-3.5-turbo-0125".
        """
        self.api_key = api_key
        self.model = model
        self.weight = weight
        self.temperature = temperature
        self.client = OpenAI(api_key=self.api_key)

    def generate_text(self, prompt: str, **kwargs: dict[str, Any]) -> str:
        """
        Generate text based on the provided prompt.

        Args:
            prompt (str): The input prompt for the LLM.
            kwargs (Dict[str, Any]): Additional parameters for text generation.

        Returns:
            str: The generated text.
        """
        # Modern OpenAI API - all models use chat completions now
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt},
                ],
                temperature=self.temperature,
            )

            if response.choices and response.choices[0].message.content:
                content = response.choices[0].message.content
                return content.strip()
            else:
                return ""
        except Exception as e:
            logging.error(f"OpenAI API error: {e}")
            return ""

    def get_response(self, prompt: str, **kwargs: dict[str, Any]) -> str:
        """
        Generate text based on the provided prompt.

        Args:
            prompt (str): The input prompt for the LLM.
            kwargs (Dict[str, Any]): Additional parameters for text generation.

        Returns:
            str: The generated text.
        """
        try:
            response = self.generate_text(prompt, **kwargs)
            logging.debug(f"Response from OpenAI: {response}")
            return response
        except Exception as e:
            logging.error(f"Error getting response from OpenAI: {e}")
            raise

    def get_model_info(self) -> dict[str, Any]:
        """
        Get information about the LLM model.

        Returns:
            Dict[str, Any]: A dictionary containing the model name and version.
        """
        return {
            "provider": "OpenAI",
            "model_name": self.model,
            "weight": self.weight,
            "version": "1.0",
        }
