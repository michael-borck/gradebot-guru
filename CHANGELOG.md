# Changelog

## [Unreleased]

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


