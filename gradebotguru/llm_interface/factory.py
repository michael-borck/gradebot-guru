from gradebotguru.llm_interface.openai_llm import OpenAILLM
from gradebotguru.llm_interface.base_llm import BaseLLM
from typing import Dict, Any


def create_llm(config: Dict[str, Any]) -> BaseLLM:
    """
    Factory function to create an LLM interface based on the specified provider.

    Args:
        config (Dict[str, Any]): Configuration dictionary containing provider and other settings.

    Returns:
        BaseLLM: An instance of the LLM interface.

    Raises:
        ValueError: If the specified provider is not supported.
    """
    provider = config.get('llm_provider', 'openai')
    if provider == 'openai':
        api_key = config.get('api_key')
        if not api_key:
            raise ValueError("API key is required for OpenAI provider")
        model = config.get('model')
        return OpenAILLM(api_key, model if model else "gpt-3.5-turbo")
    else:
        raise ValueError(f"Unsupported LLM provider: {provider}")
