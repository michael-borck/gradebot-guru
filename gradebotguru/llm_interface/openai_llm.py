import openai
from typing import Any, Dict
from gradebotguru.llm_interface.base_llm import BaseLLM

class OpenAILLM(BaseLLM):
    def __init__(self, api_key: str, model: str = "text-davinci-003"):
        self.api_key = api_key
        self.model = model
        openai.api_key = self.api_key

    def generate_text(self, prompt: str, **kwargs: Dict[str, Any]) -> str:
        response = openai.Completion.create(
            model=self.model,
            prompt=prompt,
            **kwargs
        )
        return response["choices"][0]["text"].strip()

    def get_model_info(self) -> Dict[str, Any]:
        return {
            "model_name": self.model,
            "api_key": "****"  # Mask the API key for security reasons
        }
