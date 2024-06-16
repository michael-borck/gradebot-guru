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

### Documentation
* docs: Update changelog for version 0.2.0 (31b8a37)

### Chores
* chore: Update changelog and version to 0.2.0

- Update CHANGELOG.md for version 0.2.0.
- Update version to 0.2.0 in pyproject.toml. (5e99a1f)

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

### Chores
* chore: Update changelog and version to 0.3.0

- Update CHANGELOG.md for version 0.3.0.
- Update version to 0.3.0 in pyproject.toml. (b3519f3)

## [v0.4.0] - 2024-06-15

<small>[Compare with latest](https://github.com/BARG-Curtin-University/gradebotguru/compare/v0.3.0...v0.4.0)</small>

### Documentation
* docs: Add ADR for LLM factory implementation (f556f97)
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

### Chores
* chore: Update changelog and version to 0.4.0

- Update CHANGELOG.md for version 0.4.0.
- Update version to 0.4.0 in pyproject.toml. (5804881)

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

### Documentation
* docs: initialize changelog with existing commit history (630c724)
* docs: Add ADR for LLM factory implementation (56a73b5)
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
* docs: Update changelog for version 0.2.0 (da842a0)
* docs: Add and update changelog for version 0.1.0

- Create CHANGELOG.md to manually track project changes and updates.
- Delete outdated changelog file (docs/change_log.md).
- Add new changelog file to documentation (docs/changelog.md).
- Update mkdocs.yml to include the new changelog in the documentation navigation. (3cfd004)
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
* docs: Update README with initial project details

- Add initial project details to README.md. (926bda7)
* docs: Add LICENSE file

- Add LICENSE file to the repository to specify the project's license. (588a85f)

### Chores
* chore: Update changelog and version to 0.4.0

- Update CHANGELOG.md for version 0.4.0.
- Update version to 0.4.0 in pyproject.toml. (6a18312)
* chore: Update changelog and version to 0.3.0

- Update CHANGELOG.md for version 0.3.0.
- Update version to 0.3.0 in pyproject.toml. (a82396e)
* chore: Update changelog and version to 0.2.0

- Update CHANGELOG.md for version 0.2.0.
- Update version to 0.2.0 in pyproject.toml. (beca767)
* chore: Update version to 0.1.0

- Update pyproject.toml to set the project version to 0.1.0 for the first release. (91e9f4f)
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
* chore: Initial commit

- Add .gitignore
- Add README.md (empty)
- Add pyproject.toml (3a5a7be)

### Refactoring
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

## [0.4.2] - 2024-06-15

<small>[Compare with latest](https://github.com/BARG-Curtin-University/gradebotguru/compare/0.4.1...0.4.2)</small>

## [1.0.0] - 2024-06-15

<small>[Compare with latest](https://github.com/BARG-Curtin-University/gradebotguru/compare/0.4.2...1.0.0)</small>

## [0.5.0] - 2024-06-15

<small>[Compare with latest](https://github.com/BARG-Curtin-University/gradebotguru/compare/1.0.0...0.5.0)</small>

### Documentation
* docs: add new documentation files (6e0ed88)

### Chores
* chore: add release script (fab12ec)
* chore: update configuration files (7efe081)

## [0.5.1] - 2024-06-15

<small>[Compare with latest](https://github.com/BARG-Curtin-University/gradebotguru/compare/0.5.0...0.5.1)</small>

### Documentation
* docs: add docstrings, type hints, and doctests to rubric_loader.py using StringIO for testing (e20bbf3)
* docs: add docstrings, type hints, and doctests to submission_loader.py (8f7231c)
* docs: add docstrings, type hints, and doctests to logging_config.py (a778f41)
* docs: add doctests to submission_loader.py (fdbe1cb)
* docs: add doctests to config.py (d742e40)

### Chores
* chore: replace symbolic links with actual files in the docs folder for changelog, code of conduct, contributing, and roadmap (a68a187)
* chore: add automated release script with version bumping and changelog generation (f1503a1)

## [0.5.3] - 2024-06-15

<small>[Compare with latest](https://github.com/BARG-Curtin-University/gradebotguru/compare/0.5.1...0.5.3)</small>

### Features
* feat: Implement prompt generation with type hints and comprehensive tests

- Added  with functions to generate system and user prompts.
- Enhanced prompt generation to support different assessment types (essay, code).
- Included type hints in the functions for better code clarity and type checking.
- Created comprehensive tests using pytest for prompt generation functions.
- Added docstrings to all tests for better documentation and understanding. (6c4e886)

### Documentation
* docs: Add API documentation for prompts

- Added API documentation for prompt generation in docs/api/prompts.md. (d961642)
* docs: Add ADR for improving marking consistency

- Added ADR 0011 to outline strategies for improving marking consistency using prompt engineering, response augmentation, RAG, fine-tuning, hybrid approaches, continuous improvement, multi-modal assessment, and standardized feedback templates.
- Updated mkdocs.yml to include the new ADR document. (e90ef63)
* docs: Add documentation on refactoring and code consistency

- Updated mkdocs.yml to reflect recent documentation changes.
- Added '0010-project-code-consistency.md' to explain the time spent on refactoring, consistent style, and adding docstrings.
- Ensured consistency in style and documentation across the project for better maintainability and readability. (3db390f)
* docs: update ROADMAP.md to reflect completed tasks in Phase 1 and Phase 2 (79adecb)
* docs: add docstrings, type hints, and doctests to rubric_loader.py using StringIO for testing (c58d0bc)
* docs: add docstrings, type hints, and doctests to submission_loader.py (ba03657)
* docs: add docstrings, type hints, and doctests to logging_config.py (d35c748)
* docs: add doctests to submission_loader.py (8361050)
* docs: add doctests to config.py (1bbf14a)

### Chores
* chore: bump version to 0.5.3 and update changelog (87c4a2f)
* chore: Remove duplicate documentation files with incorrect case

- Deleted , , and  as they were duplicates with incorrect casing.
- Ensured proper casing for documentation file names. (8de8d7d)
* chore: improve code consistency and project management

- Added docstrings, type hints, and doctests to various modules
- Updated release script to include 'chore' tag for version bumps
- Ensured code complies with flake8 requirements
- Enhanced readability and maintainability of the codebase (d9fa557)
* chore: update release script to include 'chore' tag in version bump commit message (3f74cc6)
* chore: Bump version to 0.5.1 and update changelog (a9a94b4)
* chore: replace symbolic links with actual files in the docs folder for changelog, code of conduct, contributing, and roadmap (87b4b8d)
* chore: add automated release script with version bumping and changelog generation (09d9560)
* chore: Bump version to 0.5.0 and update changelog (48065e7)
* chore: Bump version to 0.4.1 and update changelog (a0e50f0)
* chore: Bump version to 0.4.1 and update changelog (0ed676b)

## [0.5.4] - 2024-06-15

<small>[Compare with latest](https://github.com/BARG-Curtin-University/gradebotguru/compare/0.5.3...0.5.4)</small>

### Chores
* chore: bump version to 0.5.4 and update changelog (a55ccdd)

## [0.5.5] - 2024-06-15

<small>[Compare with latest](https://github.com/BARG-Curtin-University/gradebotguru/compare/0.5.4...0.5.5)</small>

### Features
* feat: Implement prompt generation and response parsing with tests

- Added prompt generation functions with response templates in prompts.py.
- Implemented response parsing to extract grades and feedback in response_parser.py.
- Created comprehensive tests for prompt generation in tests/test_prompts.py.
- Added tests for response parsing in tests/test_response_parser.py. (093beff)

### Documentation
* docs: Add ADR for implementing default loaders for submissions

- Added ADR 0012 to outline the implementation of default loaders for various submission formats (text, markdown, PDF, DOCX, code).
- Updated mkdocs.yml to include the new ADR document. (96ab43c)
* docs: Add ADR for implementing default loaders for submissions

- Added ADR 0012 to outline the implementation of default loaders for various submission formats (text, markdown, PDF, DOCX, code).
- Updated mkdocs.yml to include the new ADR document. (c964a83)

### Chores
* chore: bump version to 0.5.5 and update changelog (ce0f181)
* chore: delete wrong version of ROADMAP in docs folder (8082e4d)

### Refactoring
* refactor: Replace PyPDF2 with pypdf and update submission loader

- Replaced PyPDF2 with pypdf in submission_loader.py and test_submission_loader.py.
- Updated pyproject.toml and poetry.lock to include pypdf as a dependency.
- Adjusted code to use PdfWriter from pypdf instead of PdfFileWriter. (0729857)

## [0.5.6] - 2024-06-15

<small>[Compare with latest](https://github.com/BARG-Curtin-University/gradebotguru/compare/0.5.5...0.5.6)</small>

### Documentation
* docs: Add ADR to organize llm_inference as a sub-package within gradebotguru

- Documented the decision to keep llm_inference as a sub-package within gradebotguru.
- Explained the rationale, implications, and implementation details. (6219848)
* docs: Add ADR for adopting function-based design approach (3e9df58)

### Chores
* chore: bump version to 0.5.6 and update changelog (1a2312d)
* chore: deleted api.py functionality provided by factory (39abfed)
* chore: renamed basellm.py to base_llm.py (2e0a471)

### Refactoring
* refactor: Rename llm_inference to llm_interface for clarity and consistency

- Renamed llm_inference sub-package to llm_interface to better reflect its purpose as the interface for interacting with different LLMs.
- Updated all affected import statements in the codebase to reflect this change.
- Modified test files to use the updated llm_interface naming.
- Added ADR 0014 to document the decision and rationale for organizing llm_interface as a sub-package within gradebotguru. (e301261)
* refactor: Update BaseLLM abstract class and tests for improved architecture

- Refined BaseLLM abstract class with get_response, generate_text, and get_model_info methods based on a better understanding of the program's architecture.
- Updated MockLLM class for testing purposes.
- Added tests for MockLLM to verify the implementation of get_response, generate_text, and get_model_info methods. (c61be26)

## [0.5.7] - 2024-06-16

<small>[Compare with latest](https://github.com/BARG-Curtin-University/gradebotguru/compare/0.5.6...0.5.7)</small>

### Features
* feat: Update rubric_loader to handle optional descriptions and corresponding test cases (1fd4f95)
* feat: Refactor core functionality and update main workflow

- Moved core grading logic to core.py for better separation of concerns.
- Updated main.py to use core functions for processing submissions.
- Added doctests to core.py to ensure functionality.
- Updated test_main.py to correctly mock dependencies and test CLI integration.
- Added test_core.py to test core grading logic independently. (3da5762)
* feat: Update main workflow and add tests

- Updated factory.py to support the main workflow.
- Removed unnecessary local_llm.py.
- Updated openai_llm.py for improved LLM handling.
- Implemented main.py to handle CLI inputs and process submissions.
- Enhanced submission_loader.py to load all files in a directory.
- Added tests for main.py to ensure correct functionality. (adc40c2)

### Documentation
* docs: Add ADR for adoption of Semantic Versioning

- Documented the decision to adopt Semantic Versioning starting from version 0.5.0.
- Explained the rationale, implications, and implementation details. (5638e1d)

### Chores
* chore: bump version to 0.5.7 and update changelog (abd039d)
* chore: fixed name of ADR 0014 from llm-infernece to llm-interface (876e283)

### Refactoring
* refactor: Extract MockLLM into a separate test utility module

- Moved the MockLLM class to tests/test_utils.py for reuse across multiple test files. (c4e5ab2)
* refactor: Remove unnecessary gradebotguru.py

- Removed gradebotguru.py as its functionality is covered by other modules.
- Simplified project structure for better maintainability. (8f87c54)

## Unreleased

<small>[Compare with latest](https://github.com/BARG-Curtin-University/gradebotguru/compare/0.5.7...HEAD)</small>

### Features
* feat: Add support for Ollama LLM with configuration and integration (4f71180)
* feat: Add script to upload issues to GitHub from JSON file with optional config file

- Implement  to upload issues to GitHub.
- Support for configuration via  and environment variables.
- Added example  and  files for demonstration.
- Allows specifying configuration file and issues file via command-line arguments. (339ff85)
* feat: Add demo folder with sample config, rubric, and submissions, and update documentation examples (bf439be)

### Documentation
* docs: Update documentation for testing and add API documentation for all modules (85556f2)
* docs: Add documentation for admin scripts and update mkdocs configuration (d8e0506)
* docs: Update ADR 0017 with examples of categorised commit messages (e4c39cd)
* docs: Add ADR 0016 for standardized rubric schema and update mkdocs.yml (5ac8529)

### Chores
* chore: Add generate_markdown.py script for generating markdown files from Python docstrings (2d6ef27)
* chore: organize administrative scripts and files into scripts folder (72c2666)

