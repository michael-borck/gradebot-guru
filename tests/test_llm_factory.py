
import pytest

from gradebotguru.llm_interface.factory import create_llm
from gradebotguru.llm_interface.openai_llm import OpenAILLM


def test_create_openai_llm() -> None:
    """
    Test the creation of an OpenAILLM instance using the factory function.

    This test verifies that the factory function `create_llm` correctly creates an
    instance of `OpenAILLM` when provided with a valid configuration dictionary.
    The test also checks that the `api_key` and `model` attributes are set correctly.

    Raises:
        AssertionError: If the created instance is not of type `OpenAILLM` or
                        if the attributes `api_key` and `model` are not set correctly.
    """
    config: dict[str, str] = {
        "llm_type": "openai",
        "api_key": "test_key",
        "model": "text-davinci-003",
    }
    llm = create_llm(config)
    assert isinstance(llm, OpenAILLM)
    assert llm.api_key == "test_key"
    assert llm.model == "text-davinci-003"


def test_create_unsupported_llm() -> None:
    """
    Test the creation of an unsupported LLM type using the factory function.

    This test verifies that the factory function `create_llm` raises a `ValueError`
    when provided with a configuration dictionary containing an unsupported LLM type.

    Raises:
        ValueError: If the `llm_type` in the configuration dictionary is not supported.
    """
    config: dict[str, str] = {"llm_type": "unsupported", "api_key": "test_key"}
    with pytest.raises(ValueError, match="Unsupported LLM type: unsupported"):
        create_llm(config)
