import pytest
from gradebotguru.llm_inference.factory import create_llm
from gradebotguru.llm_inference.openai_llm import OpenAILLM


def test_create_openai_llm():
    config = {
        'llm_type': 'openai',
        'api_key': 'test_key',
        'model': 'text-davinci-003'
    }
    llm = create_llm(config)
    assert isinstance(llm, OpenAILLM)
    assert llm.api_key == 'test_key'
    assert llm.model == 'text-davinci-003'


def test_create_unsupported_llm():
    config = {
        'llm_type': 'unsupported',
        'api_key': 'test_key'
    }
    with pytest.raises(ValueError, match="Unsupported LLM type: unsupported"):
        create_llm(config)
