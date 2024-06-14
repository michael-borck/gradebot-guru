from abc import ABC, abstractmethod
from typing import Any, Dict


class BaseLLM(ABC):
    @abstractmethod
    def generate_text(self, prompt: str, **kwargs: Dict[str, Any]) -> str:
        """
        Generate text based on the provided prompt.

        Args:
            prompt (str): The input prompt for the LLM.
            kwargs (Dict[str, Any]): Additional parameters for text generation.

        Returns:
            str: The generated text.
        """
        pass

    @abstractmethod
    def get_model_info(self) -> Dict[str, Any]:
        """
        Get information about the LLM model.

        Returns:
            Dict[str, Any]: Information about the LLM model.
        """
        pass
