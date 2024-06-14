# ADR 0005: Use Custom LLM Interface

## Status

Accepted

## Context

GradeBot Guru requires a mechanism to interact with large language models (LLMs) for grading and providing feedback on student submissions. While there are existing libraries like Langchain and LiteLLM that provide pre-built functionalities for interacting with LLMs, there are considerations regarding complexity, dependencies, and the specific needs of our application.

## Decision

We will proceed with a custom implementation for the LLM interface for the following reasons:
1. **Simplicity:** Our application has relatively straightforward requirements for interacting with LLMs. A custom implementation provides the necessary functionality without the overhead of integrating a comprehensive library.
2. **Flexibility:** A custom implementation allows us to tailor the LLM interactions specifically to our application's needs, without being constrained by the design and limitations of external libraries.
3. **Control:** Managing our own implementation provides greater control over the functionality and behavior of the LLM interactions, making it easier to debug and maintain.
4. **Future Integration:** We will keep the option open to integrate with Langchain or LiteLLM in the future if the application's requirements become more complex and could benefit from the advanced features provided by these libraries.

### Implementation

1. **Base LLM Interface:**
   - Implement a `BaseLLM` abstract class in `llm_inference/base_llm.py` to define the basic interface for LLM interaction.
   - Implement the `generate_text` and `get_model_info` methods as abstract methods to be overridden by subclasses.

2. **OpenAI LLM Interface:**
   - Implement the `OpenAILLM` class in `llm_inference/openai_llm.py` that extends the `BaseLLM` class.
   - Implement the `generate_text` method to interact with the OpenAI API for text generation.
   - Implement the `get_model_info` method to provide information about the OpenAI model.

### Consequences

### Positive Consequences

- **Flexibility:** The custom implementation allows for tailored interactions with the LLMs specific to GradeBot Guru's needs.
- **Simplicity:** Avoids the complexity of integrating and managing external libraries.
- **Control:** Provides greater control over the functionality and behavior of LLM interactions.

### Negative Consequences

- **Reimplementation:** Some functionalities provided by external libraries may need to be reimplemented, potentially duplicating effort.
- **Maintenance:** Custom code requires ongoing maintenance and updates, particularly if the underlying LLM APIs change.

### Alternatives Considered

1. **Langchain:**
   - Pros: Comprehensive framework with advanced features.
   - Cons: Overkill for our current needs, increased complexity and dependency management.

2. **LiteLLM:**
   - Pros: Simpler interface for basic LLM interactions.
   - Cons: Still adds an external dependency, which may not be necessary for our current needs.

## Conclusion

The decision to proceed with a custom implementation for the LLM interface in GradeBot Guru is based on the current simplicity and flexibility needs of the application. This approach allows us to tailor the functionality specifically to our requirements while keeping the option open to integrate with external libraries in the future if necessary.
