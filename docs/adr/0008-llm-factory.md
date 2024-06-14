### ADR for LLM Factory

#### `docs/adr/0008-llm-factory.md`

```markdown
# ADR 0008: LLM Factory

## Status

Accepted

## Context

GradeBot Guru requires a mechanism to create instances of different large language models (LLMs) based on configuration. This is necessary to support multiple LLM providers and to ensure that the system is flexible and easily extendable. Implementing a factory pattern for LLM instances will help achieve this goal.

## Decision

We will implement a factory function named `create_llm` in `llm_inference/factory.py` that:
1. Instantiates different LLM classes based on the provided configuration.
2. Supports creating instances of the `OpenAILLM` class and can be extended to support additional LLM classes in the future.

### Implementation

1. **Define the `create_llm` Function:**

   The `create_llm` function will instantiate different LLM classes based on the provided configuration.

   ```python
   # llm_inference/factory.py

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
   ```

2. **Write Unit Tests for the LLM Factory:**

   Unit tests will ensure the factory correctly creates instances of the specified LLM classes.

   ```python
   # tests/test_factory.py

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
   ```

## Consequences

### Positive Consequences

- **Flexibility:** The factory pattern allows for easy creation of different LLM instances based on configuration.
- **Extensibility:** New LLM models can be easily integrated by extending the factory function to support additional LLM classes.
- **Maintainability:** Centralizing the creation logic in a factory function simplifies the codebase and makes it easier to manage and update.

### Negative Consequences

- **Overhead:** Introducing a factory pattern adds a small amount of complexity and overhead, especially for simple applications.
- **Dependency Management:** Ensuring that all LLM classes and their dependencies are properly managed requires careful attention.

## Alternatives Considered

1. **Direct Instantiation:**
   - Pros: Simpler initial implementation.
   - Cons: Less flexible and harder to extend for multiple LLM types.

2. **Using an External Library:**
   - Pros: Leverages existing functionality and reduces the need to reimplement common patterns.
   - Cons: Adds an external dependency and may not fully align with the specific requirements of the application.

## Conclusion

The decision to implement a factory function for creating LLM instances in `llm_inference/factory.py` provides the necessary flexibility, extensibility, and maintainability for GradeBot Guru. This approach ensures that the application can easily support multiple LLM providers and can be extended to integrate new LLM models in the future.
```

### Commit the ADR

1. **Create the ADR file:**
   Save the above content in `docs/adr/0008-llm-factory.md`.

2. **Commit the ADR:**

```sh
git add docs/adr/0008-llm-factory.md
git commit -m "docs: Add ADR for LLM factory implementation"
```