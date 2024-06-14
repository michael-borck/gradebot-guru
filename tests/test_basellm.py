import pytest
from gradebotguru.llm_inference.base_llm import BaseLLM
from typing import Any, Dict

class MockLLM(BaseLLM):
    def generate_text(self, prompt: str, **kwargs: Dict[str, Any]) -> str:
        return f"Mock response to prompt: {prompt}"

    def get_model_info(self) -> Dict[str, Any]:
        return {"model_name": "MockLLM", "version": "1.0"}

def test_generate_text():
    llm = MockLLM()
    response = llm.generate_text("Hello, world!")
    assert response == "Mock response to prompt: Hello, world!"

def test_get_model_info():
    llm = MockLLM()
    info = llm.get_model_info()
    assert info == {"model_name": "MockLLM", "version": "1.0"}
