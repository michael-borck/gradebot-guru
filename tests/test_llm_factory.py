from typing import Any

import pytest

from gradebotguru.llm_interface.factory import create_llms
from gradebotguru.llm_interface.openai_llm import OpenAILLM


def test_create_openai_llm() -> None:
    """
    Test the creation of OpenAI LLM instances using the factory function.

    This test verifies that the factory function `create_llms` correctly creates
    instances of `OpenAILLM` when provided with a valid configuration dictionary.
    The test also checks that the `api_key` and `model` attributes are set correctly.

    Raises:
        AssertionError: If the created instance is not of type `OpenAILLM` or
                        if the attributes `api_key` and `model` are not set correctly.
    """
    config: dict[str, Any] = {
        "llm_providers": [
            {
                "provider": "openai",
                "api_key": "test_key",
                "model": "gpt-3.5-turbo",
                "temperature": 0.7,
                "weight": 1.0,
            }
        ]
    }
    llms = create_llms(config)
    assert len(llms) == 1
    assert isinstance(llms[0], OpenAILLM)
    assert llms[0].api_key == "test_key"
    assert llms[0].model == "gpt-3.5-turbo"


def test_create_unsupported_llm() -> None:
    """
    Test the creation of an unsupported LLM provider using the factory function.

    This test verifies that the factory function `create_llms` raises a `ValueError`
    when provided with a configuration dictionary containing an unsupported LLM provider.

    Raises:
        ValueError: If the `provider` in the configuration dictionary is not supported.
    """
    config: dict[str, Any] = {
        "llm_providers": [{"provider": "unsupported", "api_key": "test_key"}]
    }
    with pytest.raises(ValueError, match="Unsupported LLM provider: unsupported"):
        create_llms(config)
