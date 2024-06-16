from gradebotguru.llm_interface.base_llm import BaseLLM
from gradebotguru.llm_interface.openai_llm import OpenAILLM
from gradebotguru.llm_interface.local_llm import OllamaLLM
from typing import Dict, Any


def create_llm(config: Dict[str, Any]) -> BaseLLM:
    """
    Factory function to create an LLM instance based on the provided configuration.

    Args:
        config (Dict[str, Any]): Configuration dictionary containing LLM settings.

    Returns:
        BaseLLM: An instance of the appropriate LLM class.

    Raises:
        ValueError: If an unsupported LLM provider is specified.
    """
    provider = config.get('llm_provider', 'openai')
    if provider == 'openai':
        api_key = config.get('api_key')
        if not api_key:
            raise ValueError("API key is required for OpenAI provider")
        model = config.get('llm_model', 'text-davinci-003')
        return OpenAILLM(api_key, model)
    elif provider == 'ollama':
        api_key = config.get('api_key', 'ollama')  # required, but unused
        server_url = config.get('server_url', 'http://localhost:11434/v1')
        model = config.get('llm_model', 'llama3')
        return OllamaLLM(api_key, server_url, model)
    else:
        raise ValueError(f"Unsupported LLM provider: {provider}")
