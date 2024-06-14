# ADR 0006: Base LLM Interface

## Status

Accepted

## Context

GradeBot Guru requires a flexible and extensible mechanism to interact with different large language models (LLMs). To achieve this, a base class should be defined that specifies the essential methods for interacting with LLMs. This will allow different LLM implementations to inherit from this base class and provide their specific implementations while maintaining a consistent interface.

## Decision

We will implement a base class named `BaseLLM` in `base_llm.py` that:
1. Defines abstract methods for text generation and retrieving model information.
2. Provides a consistent interface for interacting with various LLM implementations.

### Implementation

1. **Define the Base Class:**

   The `BaseLLM` class will be defined as an abstract base class (ABC) with abstract methods for text generation and retrieving model information.

   ```python
   # base_llm.py

   from abc import ABC, abstractmethod
   from typing import Any, Dict

   class BaseLLM(ABC):
       @abstractmethod
       def generate_text(self, prompt: str, **kwargs: Dict[str, Any]) -> str:
           """
           Generate text based on the provided prompt.

           Args:
               prompt (str): The input prompt for the LLM.
               kwargs (Dict[str, Any]): Additional parameters for text generation.

           Returns:
               str: The generated text.
           """
           pass

       @abstractmethod
       def get_model_info(self) -> Dict[str, Any]:
           """
           Get information about the LLM model.

           Returns:
               Dict[str, Any]: Information about the LLM model.
           """
           pass
   ```

2. **Implement Mock LLM for Testing:**

   A mock LLM implementation will be created to test the base class.

   ```python
   # tests/test_base_llm.py

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
   ```

## Consequences

### Positive Consequences

- **Flexibility:** The base class allows for different LLM implementations to be developed independently while maintaining a consistent interface.
- **Extensibility:** New LLM models can be easily integrated by inheriting from the base class and implementing the required methods.
- **Testability:** The abstract methods ensure that any subclass provides the necessary functionality, making it easier to test and validate implementations.

### Negative Consequences

- **Complexity:** Introducing an abstract base class adds a level of abstraction, which may increase the complexity of the codebase.
- **Overhead:** Subclasses must implement all abstract methods, which could lead to some redundancy if multiple LLMs share common functionality.

## Alternatives Considered

1. **Direct Implementation:**
   - Implementing LLM interactions directly without an abstract base class would reduce initial complexity but would make it harder to integrate new LLM models consistently.

2. **Using a Simple Interface:**
   - Defining a simple interface with concrete methods could reduce flexibility and make it harder to enforce consistent behavior across different LLM implementations.

## Conclusion

The chosen approach of implementing the `BaseLLM` abstract base class in `base_llm.py` provides the necessary flexibility, extensibility, and testability for interacting with various large language models in GradeBot Guru. This decision ensures that the application can easily integrate and utilize different LLM models while maintaining a consistent and testable interface.