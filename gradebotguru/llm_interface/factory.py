from gradebotguru.llm_interface.base_llm import BaseLLM
from gradebotguru.llm_interface.openai_llm import OpenAILLM
from gradebotguru.llm_interface.local_llm import OllamaLLM
from typing import Dict, Any


def create_llm(provider_config: Dict[str, Any]) -> BaseLLM:
    """
    Factory function to create an LLM instance based on the provided configuration.

    Args:
        provider_config (Dict[str, Any]): Configuration dictionary containing LLM settings.

    Returns:
        BaseLLM: An instance of the appropriate LLM class.

    Raises:
        ValueError: If an unsupported LLM provider is specified.
    """
    provider = provider_config.get('provider', 'openai')
    if provider == 'openai':
        api_key = provider_config.get('api_key')
        if not api_key:
            raise ValueError("API key is required for OpenAI provider")
        model = provider_config.get('model', 'text-davinci-003')
        return OpenAILLM(api_key, model)
    elif provider == 'ollama':
        api_key = provider_config.get('api_key', 'ollama')  # required, but unused
        server_url = provider_config.get('server_url', 'http://localhost:11434/v1')
        model = provider_config.get('model', 'llama3')
        return OllamaLLM(api_key, server_url, model)
    else:
        raise ValueError(f"Unsupported LLM provider: {provider}")


def create_llms(config: Dict[str, Any]) -> Dict[str, BaseLLM]:
    """
    Factory function to create multiple LLM instances based on the provided configuration.

    Args:
        config (Dict[str, Any]): Configuration dictionary containing LLM settings.

    Returns:
        Dict[str, BaseLLM]: A dictionary of LLM instances with provider names as keys.

    Raises:
        ValueError: If an unsupported LLM provider is specified.
    """
    llm_providers_config = config.get('llm_providers', [])
    llms = {}
    for provider_config in llm_providers_config:
        provider_name = provider_config.get('provider', 'unknown_provider')
        llms[provider_name] = create_llm(provider_config)
    return llms
