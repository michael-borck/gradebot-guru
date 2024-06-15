# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [v0.2.0] - 2024-06-14

<small>[Compare with latest](https://github.com/BARG-Curtin-University/gradebotguru/compare/v0.1.0...v0.2.0)</small>

### Features
* feat: Implement submission loader and unit tests

- Add load_submissions function in submission_loader.py to load and parse student submissions from a directory.
- Ensure the function reads files from a given directory and returns their contents in a dictionary.
- Write unit tests for the load_submissions function using pytest and pytest-mock.

The load_submissions function ensures that student submissions are correctly loaded and parsed, forming an essential part of the grading process in GradeBot Guru. (245bfbd)
* feat: Implement rubric loader and unit tests

- Add load_rubric function in rubric_loader.py to load and parse grading rubric from a CSV file.
- Define the rubric schema with criteria and weights.
- Write unit tests for the load_rubric function using pytest and pytest-mock.

The load_rubric function ensures that grading rubrics are correctly loaded and parsed, forming a crucial part of the grading logic in GradeBot Guru. (00b7a59)
### Others
* chore: Update changelog and version to 0.2.0

- Update CHANGELOG.md for version 0.2.0.
- Update version to 0.2.0 in pyproject.toml. (5e99a1f)
* docs: Update changelog for version 0.2.0 (31b8a37)
* Update version to 0.1.0 (23fb192)

## [v0.3.0] - 2024-06-14

<small>[Compare with latest](https://github.com/BARG-Curtin-University/gradebotguru/compare/v0.2.0...v0.3.0)</small>

### Features
* feat: Implement OpenAI LLM interface and unit tests

- Add OpenAILLM class in llm_inference/openai_llm.py that extends the BaseLLM class.
- Implement generate_text method to interact with the OpenAI API for text generation.
- Implement get_model_info method to provide information about the OpenAI model.
- Write unit tests for the OpenAILLM class methods using pytest and pytest-mock.

The OpenAILLM class provides a concrete implementation for interacting with the OpenAI API, enabling text generation and model information retrieval within GradeBot Guru. (6a6210e)
* feat: Implement base LLM interface and unit tests

- Add BaseLLM abstract class in llm_inference/base_llm.py to define the basic interface for LLM interaction.
- Define abstract methods generate_text and get_model_info in BaseLLM class.
- Implement MockLLM class in tests/test_base_llm.py to test the base LLM interface.
- Write unit tests for the BaseLLM class methods using pytest.

The BaseLLM class provides a consistent and extensible interface for interacting with various large language models in GradeBot Guru. (c009c6e)
### Others
* chore: Update changelog and version to 0.3.0

- Update CHANGELOG.md for version 0.3.0.
- Update version to 0.3.0 in pyproject.toml. (b3519f3)

## [v0.4.0] - 2024-06-15

<small>[Compare with latest](https://github.com/BARG-Curtin-University/gradebotguru/compare/v0.3.0...v0.4.0)</small>

### Others
* docs: Add ADR for LLM factory implementation (f556f97)
* chore: Update changelog and version to 0.4.0

- Update CHANGELOG.md for version 0.4.0.
- Update version to 0.4.0 in pyproject.toml. (5804881)
* docs: Renumbered LLM interface ADRs (3fac245)
* docs: Add ADR for using custom LLM interface (dbf62ab)
* docs: Add API documentation using mkdocstrings

- Add mkdocstrings plugin to mkdocs.yml with Python handler.
- Create API documentation files for each module:
  - Configuration: api/config.md
  - Rubric Loader: api/rubric_loader.md
  - Submission Loader: api/submission_loader.md
  - Base LLM: api/base_llm.md
  - OpenAI LLM: api/openai_llm.md
- Update mkdocs.yml to include API documentation in the navigation.
- Ensure API documentation is generated from docstrings.

This update adds comprehensive API documentation for the GradeBot Guru project, making it easier for developers to understand and use the implemented modules. (8c62b67)

## [0.4.1] - 2024-06-15

<small>[Compare with latest](https://github.com/BARG-Curtin-University/gradebotguru/compare/v0.4.0...0.4.1)</small>

### Features
* feat: Implement LLM factory in factory.py

- Add create_llm function to instantiate different LLM classes based on configuration. (d2c343d)
* feat: Implement OpenAI LLM interface and unit tests

- Add OpenAILLM class in llm_inference/openai_llm.py that extends the BaseLLM class.
- Implement generate_text method to interact with the OpenAI API for text generation.
- Implement get_model_info method to provide information about the OpenAI model.
- Write unit tests for the OpenAILLM class methods using pytest and pytest-mock.

The OpenAILLM class provides a concrete implementation for interacting with the OpenAI API, enabling text generation and model information retrieval within GradeBot Guru. (757a66e)
* feat: Implement base LLM interface and unit tests

- Add BaseLLM abstract class in llm_inference/base_llm.py to define the basic interface for LLM interaction.
- Define abstract methods generate_text and get_model_info in BaseLLM class.
- Implement MockLLM class in tests/test_base_llm.py to test the base LLM interface.
- Write unit tests for the BaseLLM class methods using pytest.

The BaseLLM class provides a consistent and extensible interface for interacting with various large language models in GradeBot Guru. (2f619de)
* feat: Implement submission loader and unit tests

- Add load_submissions function in submission_loader.py to load and parse student submissions from a directory.
- Ensure the function reads files from a given directory and returns their contents in a dictionary.
- Write unit tests for the load_submissions function using pytest and pytest-mock.

The load_submissions function ensures that student submissions are correctly loaded and parsed, forming an essential part of the grading process in GradeBot Guru. (31a31f6)
* feat: Implement rubric loader and unit tests

- Add load_rubric function in rubric_loader.py to load and parse grading rubric from a CSV file.
- Define the rubric schema with criteria and weights.
- Write unit tests for the load_rubric function using pytest and pytest-mock.

The load_rubric function ensures that grading rubrics are correctly loaded and parsed, forming a crucial part of the grading logic in GradeBot Guru. (0baad46)
* feat: Implement configuration loader

- Implement configuration loader in gradebotguru/config.py to load and parse configuration settings.
- Add ADR for configuration loader implementation (docs/adr/0001-configuration-loader.md).
- Update architecture documentation to include configuration loader details (docs/architecture.md).
- Add unit tests for the configuration loader (tests/test_config.py). (34bb409)
* feat: Add issue templates and update code stubs

- Add GitHub issue templates for feature requests and tasks:
  - .github/ISSUE_TEMPLATE/feature_request.md
  - .github/ISSUE_TEMPLATE/task.md
- Update and refine stubs for core modules:
  - Modified: gradebotguru/config.py
  - Modified: gradebotguru/grader.py
  - Modified: gradebotguru/llm_inference/base_llm.py
  - Modified: gradebotguru/llm_inference/factory.py
  - Modified: gradebotguru/llm_inference/openai.py
  - Modified: gradebotguru/logging_config.py
  - Modified: gradebotguru/main.py
  - Modified: gradebotguru/prompts.py
  - Modified: gradebotguru/response_parser.py
  - Modified: gradebotguru/rubric_loader.py
- Correct file naming:
  - Deleted: gradebotguru/submission_loader.py
  - Added: gradebotguru/submissions_loader.py (7e357be)
* feat: Add skeleton code for core modules and tests

- Add skeleton code for core application modules:
  - gradebotguru/config.py
  - gradebotguru/gradebotguru.py
  - gradebotguru/grader.py
  - gradebotguru/logging_config.py
  - gradebotguru/main.py
  - gradebotguru/prompts.py
  - gradebotguru/response_parser.py
  - gradebotguru/rubric_loader.py
  - gradebotguru/submission_loader.py
- Add skeleton code for LLM inference modules:
  - gradebotguru/llm_inference/api.py
  - gradebotguru/llm_inference/base_llm.py
  - gradebotguru/llm_inference/factory.py
  - gradebotguru/llm_inference/gemini.py
  - gradebotguru/llm_inference/local_llm.py
  - gradebotguru/llm_inference/openai.py
- Add skeleton code for test modules:
  - tests/integration/__init__.py
  - tests/integration/test_integration.py
  - tests/test_grader.py
  - tests/test_llm_interface.py
  - tests/test_prompts.py
  - tests/test_response_parser.py
  - tests/test_rubric_loader.py
  - tests/test_submission_loader.py (b8f50d8)
### Others
* Bump version to 0.4.1 and update changelog (39c09cb)
* docs: initialize changelog with existing commit history (630c724)
* docs: Add ADR for LLM factory implementation (56a73b5)
* chore: Update changelog and version to 0.4.0

- Update CHANGELOG.md for version 0.4.0.
- Update version to 0.4.0 in pyproject.toml. (6a18312)
* docs: Renumbered LLM interface ADRs (d3c258c)
* docs: Add ADR for using custom LLM interface (4c2007d)
* docs: Add API documentation using mkdocstrings

- Add mkdocstrings plugin to mkdocs.yml with Python handler.
- Create API documentation files for each module:
  - Configuration: api/config.md
  - Rubric Loader: api/rubric_loader.md
  - Submission Loader: api/submission_loader.md
  - Base LLM: api/base_llm.md
  - OpenAI LLM: api/openai_llm.md
- Update mkdocs.yml to include API documentation in the navigation.
- Ensure API documentation is generated from docstrings.

This update adds comprehensive API documentation for the GradeBot Guru project, making it easier for developers to understand and use the implemented modules. (64e9d23)
* chore: Update changelog and version to 0.3.0

- Update CHANGELOG.md for version 0.3.0.
- Update version to 0.3.0 in pyproject.toml. (a82396e)
* chore: Update changelog and version to 0.2.0

- Update CHANGELOG.md for version 0.2.0.
- Update version to 0.2.0 in pyproject.toml. (beca767)
* docs: Update changelog for version 0.2.0 (da842a0)
* chore: Update version to 0.1.0

- Update pyproject.toml to set the project version to 0.1.0 for the first release. (91e9f4f)
* docs: Add and update changelog for version 0.1.0

- Create CHANGELOG.md to manually track project changes and updates.
- Delete outdated changelog file (docs/change_log.md).
- Add new changelog file to documentation (docs/changelog.md).
- Update mkdocs.yml to include the new changelog in the documentation navigation. (3cfd004)
* refactor: Add docstrings and type hints to existing code

- Add docstrings and type hints to enhance code readability and maintainability:
  - Modified: gradebotguru/config.py
  - Modified: gradebotguru/logging_config.py
  - Modified: tests/test_config.py
- Add ADR for logging configuration implementation (docs/adr/0002-logging-configuration.md).
- Update ADR for configuration loader to include type hints and docstrings (docs/adr/0001-configuration-loader.md).
- Update project dependencies and settings:
  - Modified: poetry.lock
  - Modified: pyproject.toml
- Add unit tests for logging configuration (tests/test_logging.py). (e94887a)
* docs: Setup initial documentation structure

- Add bug report and pull request templates:
  - .github/ISSUE_TEMPLATE/bug_report.md
  - .github/PULL_REQUEST_TEMPLATE.md
- Update CONTRIBUTING.md and README.md with initial project details
- Add ROADMAP.md to outline project milestones and goals
- Add ADR example and template:
  - docs/adr/adr_001_example.md
  - docs/adr/adr_template.md
- Add initial API documentation overview (docs/api/overview.md)
- Add various documentation files:
  - docs/architecture.md
  - docs/change_log.md
  - docs/code_of_conduct.md
  - docs/contributing.md
  - docs/developer_guide.md
  - docs/examples/prompts.md
  - docs/examples/rubric.md
  - docs/examples/submissions.md
  - docs/index.md (modified)
  - docs/installation.md
  - docs/roadmap.md
  - docs/srs.md
  - docs/user_guide.md
- Delete unnecessary JavaScript files (katex.js, mathjax.js)
- Update mkdocs.yml to include the new documentation structure
- Add poetry.lock for dependency management
- Modify pyproject.toml with project dependencies and settings (cd851f3)
* chore: Setup initial project environment and structure

- Add GitHub Actions CI workflow (.github/workflows/ci.yml)
- Add project documentation and guidelines:
  - CODE_OF_CONDUCT.md
  - CONTRIBUTING.md
  - docs/index.md
- Add JavaScript files for documentation (katex.js, mathjax.js)
- Initialize gradebotguru package and subpackage (__init__.py files)
- Update README.md with initial project details
- Add mkdocs.yml for MkDocs configuration
- Modify pyproject.toml with project dependencies and settings
- Initialize tests package (__init__.py file) (4d7cef1)
* docs: Update README with initial project details

- Add initial project details to README.md. (926bda7)
* docs: Add LICENSE file

- Add LICENSE file to the repository to specify the project's license. (588a85f)
* chore: Initial commit

- Add .gitignore
- Add README.md (empty)
- Add pyproject.toml (3a5a7be)

## [0.4.2] - 2024-06-15

<small>[Compare with latest](https://github.com/BARG-Curtin-University/gradebotguru/compare/0.4.1...0.4.2)</small>

### Others
* Bump version to 0.4.2 and update changelog (b0632c5)

## [1.0.0] - 2024-06-15

<small>[Compare with latest](https://github.com/BARG-Curtin-University/gradebotguru/compare/0.4.2...1.0.0)</small>

### Others
* Bump version to 1.0.0 and update changelog (bf9ad3b)

## Unreleased

<small>[Compare with latest](https://github.com/BARG-Curtin-University/gradebotguru/compare/1.0.0...HEAD)</small>

### Others
* Bump version to 0.4.1 and update changelog (02da346)
* chore: add release script (fab12ec)
* docs: add new documentation files (6e0ed88)
* chore: update configuration files (7efe081)

