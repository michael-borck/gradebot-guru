import pytest
from pytest_mock import MockerFixture
from gradebotguru.llm_inference.openai_llm import OpenAILLM


@pytest.fixture
def mock_openai(mocker: MockerFixture):
    mocker.patch("openai.Completion.create", return_value={
        "choices": [{"text": "Mock response"}]
    })


def test_generate_text(mock_openai):
    llm = OpenAILLM(api_key="test_key")
    response = llm.generate_text("Hello, world!")
    assert response == "Mock response"


def test_get_model_info():
    llm = OpenAILLM(api_key="test_key")
    info = llm.get_model_info()
    assert info == {"model_name": "text-davinci-003", "api_key": "****"}
