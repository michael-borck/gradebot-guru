# Changelog

## [Unreleased]

## [0.4.0] - 2023-06-14
### Added
- Implement LLM factory in `llm_inference/factory.py` to create instances of different LLM classes.
- Add unit tests for the LLM factory to ensure correct instance creation.
- Add ADR for LLM factory implementation.

## [0.3.0] - 2023-06-14
### Added
- Implement OpenAI LLM interface in `llm_inference/openai_llm.py` to extend the `BaseLLM` class.
- Implement `generate_text` method to interact with the OpenAI API for text generation.
- Implement `get_model_info` method to provide information about the OpenAI model.
- Write unit tests for the `OpenAILLM` class methods using `pytest` and `pytest-mock`.

## [0.2.0] - 2023-06-14
### Added
- Implement submission loader in `submission_loader.py` to load and parse student submissions from a directory.
- Added unit tests for the `load_submissions` function using `pytest` and `pytest-mock`.
- Implemented rubric loader in `rubric_loader.py` to load and parse grading rubrics from a CSV file.
- Added unit tests for the `load_rubric` function using `pytest` and `pytest-mock`.

### Changed
- Updated project to use `pytest-mock` instead of `unittest.mock`.


## [0.1.0] - 2023-06-14
### Added
- Implemented configuration loader with default schema and environment variable overrides.
- Added unit tests for configuration loader using `pytest` and `pytest-mock`.
- Implemented logging configuration with `setup_logging` function.
- Added unit tests for logging configuration using `pytest` and `pytest-mock`.

### Changed
- Removed dependency on `unittest`.


