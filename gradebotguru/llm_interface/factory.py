# factory.py
from typing import Dict, Any, List
from gradebotguru.llm_interface.base_llm import BaseLLM
from gradebotguru.llm_interface.openai_llm import OpenAILLM
from gradebotguru.llm_interface.local_llm import OllamaLLM


def create_llms(config: Dict[str, Any]) -> List[BaseLLM]:
    """
    Factory function to create a list of LLM instances based on the provided configuration.

    Args:
        config (Dict[str, Any]): Configuration dictionary containing LLM settings.

    Returns:
        List[BaseLLM]: A list of LLM instances.

    Raises:
        ValueError: If an unsupported LLM provider is specified.
    """
    llms = []
    for provider_config in config['llm_providers']:
        provider = provider_config.get('provider', 'openai')
        if provider == 'openai':
            api_key = provider_config.get('api_key')
            if not api_key:
                raise ValueError("API key is required for OpenAI provider")
            model = provider_config.get('model', 'chatgpt-3.5-turbo')
            temperature = provider_config.get('temperature', 0.7)
            weight = provider_config.get('weight', 1.0)
            llms.append(OpenAILLM(api_key, model, temperature, weight))
        elif provider == 'ollama':
            api_key = provider_config.get('api_key', 'ollama')  # required, but unused
            server_url = provider_config.get('server_url', 'http://localhost:11434/v1')
            model = provider_config.get('model', 'llama3')
            weight = provider_config.get('weight', 1.0)
            llms.append(OllamaLLM(api_key, server_url, model, weight))
        else:
            raise ValueError(f"Unsupported LLM provider: {provider}")

    return llms
