# ADR 0007: OpenAI LLM Interface

## Status

Accepted

## Context

GradeBot Guru requires the ability to interact with various large language models (LLMs). To facilitate this, we need to implement a specific interface for the OpenAI LLM. This interface will extend the base LLM interface and provide concrete implementations for generating text and retrieving model information using the OpenAI API.

## Decision

We will implement a class named `OpenAILLM` in `llm_inference/openai_llm.py` that:
1. Extends the `BaseLLM` abstract class.
2. Implements the `generate_text` method to interact with the OpenAI API for text generation.
3. Implements the `get_model_info` method to provide information about the OpenAI model.

### Implementation

1. **Create the OpenAI LLM Class:**

   The `OpenAILLM` class will extend the `BaseLLM` class and implement the required methods.

   ```python
   # llm_inference/openai_llm.py

   import openai
   from typing import Any, Dict
   from gradebotguru.llm_inference.base_llm import BaseLLM

   class OpenAILLM(BaseLLM):
       def __init__(self, api_key: str, model: str = "text-davinci-003"):
           self.api_key = api_key
           self.model = model
           openai.api_key = self.api_key

       def generate_text(self, prompt: str, **kwargs: Dict[str, Any]) -> str:
           response = openai.Completion.create(
               model=self.model,
               prompt=prompt,
               **kwargs
           )
           return response["choices"][0]["text"].strip()

       def get_model_info(self) -> Dict[str, Any]:
           return {
               "model_name": self.model,
               "api_key": "****"  # Mask the API key for security reasons
           }
   ```

2. **Write Unit Tests for the OpenAI LLM Interface:**

   We will write unit tests to ensure the `OpenAILLM` class works correctly.

   ```python
   # tests/test_openai_llm.py

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
   ```

## Consequences

### Positive Consequences

- **Flexibility:** The OpenAILLM class allows for specific interactions with the OpenAI API, providing tailored implementations for text generation and model information retrieval.
- **Extensibility:** New LLM models from OpenAI can be easily integrated by extending the base class and implementing the required methods.
- **Testability:** The implementation is easily testable with mock API responses, ensuring reliability and correctness.

### Negative Consequences

- **Dependency:** The implementation relies on the OpenAI API, which introduces an external dependency and potential issues related to API changes or availability.
- **API Key Management:** Secure management of API keys is required to prevent unauthorized access and usage.

## Alternatives Considered

1. **Direct Integration:**
   - Directly integrating with the OpenAI API without using a base class would reduce initial complexity but would make it harder to integrate other LLM models consistently.

2. **Using a Generic API Client:**
   - Using a generic API client would provide more flexibility but would require additional abstraction layers to handle different LLM models.

## Conclusion

The chosen approach of implementing the `OpenAILLM` class in `llm_inference/openai_llm.py` provides the necessary flexibility, extensibility, and testability for interacting with the OpenAI API. This decision ensures that GradeBot Guru can easily integrate and utilize the OpenAI LLM while maintaining a consistent and testable interface.
