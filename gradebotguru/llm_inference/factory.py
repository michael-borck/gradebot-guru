from typing import Any, Dict
from gradebotguru.llm_inference.base_llm import BaseLLM
from gradebotguru.llm_inference.openai_llm import OpenAILLM


def create_llm(config: Dict[str, Any]) -> BaseLLM:
    """
    Factory function to create an instance of a specified LLM class.

    Args:
        config (Dict[str, Any]): Configuration dictionary containing LLM type and parameters.

    Returns:
        BaseLLM: An instance of the specified LLM class.
    """
    llm_type = config.get('llm_type')

    if llm_type == 'openai':
        return OpenAILLM(api_key=config['api_key'], model=config.get('model', 'text-davinci-003'))
    else:
        raise ValueError(f"Unsupported LLM type: {llm_type}")
