from tests.test_utils import MockLLM


def test_generate_text() -> None:
    """
    Test the generate_text method of MockLLM.

    This test verifies that the generate_text method returns the expected
    mock response for a given prompt.
    """
    llm = MockLLM()
    response = llm.generate_text("Hello, world!")
    assert response == "Mock response to prompt: Hello, world!"


def test_get_model_info() -> None:
    """
    Test the get_model_info method of MockLLM.

    This test verifies that the get_model_info method returns the expected
    mock model information.
    """
    llm = MockLLM()
    info = llm.get_model_info()
    assert info == {"model_name": "mock-model", "version": "1.0"}
