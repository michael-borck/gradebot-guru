import openai
import logging
from gradebotguru.llm_interface.base_llm import BaseLLM
from typing import Any, Dict


class OpenAILLM(BaseLLM):
    def __init__(self, api_key: str, model: str = "gpt-3.5-turbo-0125", temperature: float = 0.7 , weight: float = 1.0):
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
        openai.api_key = self.api_key

    def generate_text(self, prompt: str, **kwargs: Dict[str, Any]) -> str:
        """
        Generate text based on the provided prompt.

        Args:
            prompt (str): The input prompt for the LLM.
            kwargs (Dict[str, Any]): Additional parameters for text generation.

        Returns:
            str: The generated text.
        """
        if "turbo" in self.model or "gpt-4" in self.model:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": prompt}],
                **kwargs
            )
            return response.choices[0].message["content"].strip()
        else:
            response = openai.Completion.create(
                model=self.model,
                prompt=prompt,
                **kwargs
            )
            return response.choices[0].text.strip()

    def get_response(self, prompt: str, **kwargs: Dict[str, Any]) -> str:
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

    def get_model_info(self) -> Dict[str, Any]:
        """
        Get information about the LLM model.

        Returns:
            Dict[str, Any]: A dictionary containing the model name and version.
        """
        return {
            "provider": "OpenAI",
            "model_name": self.model,
            "weight": self.weight,
            "version": "1.0"
        }
