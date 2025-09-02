import pytest

from gradebotguru.llm_interface.local_llm import OllamaLLM


@pytest.fixture
def mock_ollama_llm():
    """
    Fixture to create a mock instance of OllamaLLM.

    Returns:
        OllamaLLM: An instance of OllamaLLM with mock configuration.
    """
    return OllamaLLM(
        api_key="test_key", server_url="http://localhost:11434/v1", model="llama3"
    )


def test_generate_text(mock_ollama_llm, mocker):
    """
    Test the generate_text method of OllamaLLM.

    Args:
        mock_ollama_llm (OllamaLLM): The mock instance of OllamaLLM.
        mocker (MockerFixture): The pytest-mock fixture to mock dependencies.

    Asserts:
        The response from generate_text matches the expected mock response.
    """
    mock_response = {"choices": [{"message": {"content": "This is a test response."}}]}
    mocker.patch("openai.ChatCompletion.create", return_value=mock_response)

    prompt = "Test prompt"
    response = mock_ollama_llm.generate_text(prompt)
    assert response == "This is a test response."


def test_get_response(mock_ollama_llm, mocker):
    """
    Test the get_response method of OllamaLLM.

    Args:
        mock_ollama_llm (OllamaLLM): The mock instance of OllamaLLM.
        mocker (MockerFixture): The pytest-mock fixture to mock dependencies.

    Asserts:
        The response from get_response matches the expected mock response.
    """
    mock_response = {"choices": [{"message": {"content": "This is a test response."}}]}
    mocker.patch("openai.ChatCompletion.create", return_value=mock_response)

    prompt = "Test prompt"
    response = mock_ollama_llm.get_response(prompt)
    assert response == "This is a test response."


def test_get_model_info(mock_ollama_llm):
    """
    Test the get_model_info method of OllamaLLM.

    Args:
        mock_ollama_llm (OllamaLLM): The mock instance of OllamaLLM.

    Asserts:
        The model information returned by get_model_info matches the expected values.
    """
    info = mock_ollama_llm.get_model_info()
    assert info["model_name"] == "llama3"
    assert info["api_key"] == "test_key"
    assert info["server_url"] == "http://localhost:11434/v1"
