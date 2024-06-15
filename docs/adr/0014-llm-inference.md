### ADR 0014: Organise llm_inference as a Sub-Package within gradebotguru

#### Context

To maintain a clear and organized structure within the GradeBotGuru project, we need to decide on the placement of the `llm_inference` module. The options are:

1. **Keep `llm_inference` at the same level as `gradebotguru`.**
2. **Organize `llm_inference` as a sub-package within `gradebotguru`.**

#### Decision

We decided to organize `llm_inference` as a sub-package within `gradebotguru`.

#### Rationale

1. **Organization**: Keeping related modules together helps in understanding the project structure and maintaining it.
2. **Encapsulation**: Encapsulating all LLM-related code within a specific sub-package is beneficial for modularity and maintainability.
3. **Relative Imports**: It simplifies relative imports, reducing potential issues with import paths.
4. **Industry Best Practice**: This approach follows industry best practices for structuring Python projects, ensuring that the project is easy to navigate and maintain.

#### Implications

1. **Project Structure**: All LLM-related modules are contained within the `llm_inference` sub-package, making the project structure more intuitive.
2. **Ease of Maintenance**: Encapsulation and organization improve the maintainability of the codebase.
3. **Consistency**: Future modules and sub-packages can follow this organizational pattern for consistency.

#### Implementation

The `gradebotguru` directory will include the following structure:

```
gradebotguru/
├── __init__.py
├── config.py
├── gradebotguru.py
├── grader.py
├── llm_inference/
│   ├── __init__.py
│   ├── base_llm.py
│   ├── factory.py
│   ├── local_llm.py
│   └── openai_llm.py
├── logging_config.py
├── main.py
├── prompts.py
├── response_parser.py
├── rubric_loader.py
├── submission_loader.py
