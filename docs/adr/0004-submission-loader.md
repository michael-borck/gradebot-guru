# ADR 0004: Submission Loader

## Status

Accepted

## Context

GradeBot Guru needs a mechanism to load and parse student submissions from various formats (e.g., text files, PDFs, code files) into a consistent format that can be used for grading. This functionality is essential for processing student work and providing feedback based on the rubric.

## Decision

We will implement a function named `load_submissions` in `submission_loader.py` that:
1. Loads submissions from a specified directory.
2. Parses the submissions into a dictionary where keys are filenames and values are the content of the submissions.

### Implementation

1. **Define the Submission Schema:**

   Submissions will be stored in a directory, with each submission as a separate file. For simplicity, we will assume that submissions are text files.

2. **Implement the `load_submissions` Function:**

   The `load_submissions` function will read files from the specified directory and parse their contents into a dictionary.

   ```python
   # submission_loader.py

   import os
   from typing import Dict

   def load_submissions(directory: str) -> Dict[str, str]:
       """
       Load and parse student submissions from a directory.

       Args:
           directory (str): Path to the directory containing submissions.

       Returns:
           Dict[str, str]: A dictionary where keys are filenames and values are the content of the submissions.
       """
       submissions = {}
       for filename in os.listdir(directory):
           file_path = os.path.join(directory, filename)
           if os.path.isfile(file_path):
               with open(file_path, 'r', encoding='utf-8') as file:
                   submissions[filename] = file.read()
       return submissions
   ```

3. **Write Unit Tests for the Submission Loader:**

   We will write unit tests to ensure the `load_submissions` function works correctly.

   ```python
   # tests/test_submission_loader.py

   import os
   import pytest
   from pytest_mock import MockerFixture
   from gradebotguru.submission_loader import load_submissions

   def test_load_submissions(mocker: MockerFixture) -> None:
       """
       Test loading and parsing submissions from a directory.

       Mocks the presence of files in a directory and checks if `load_submissions`
       correctly reads and parses the files.
       """
       mock_files = {
           'submission1.txt': 'This is the content of submission 1.',
           'submission2.txt': 'This is the content of submission 2.'
       }

       def mock_listdir(directory: str) -> List[str]:
           return list(mock_files.keys())

       def mock_isfile(path: str) -> bool:
           return path.split(os.sep)[-1] in mock_files

       def mock_open_func(filepath: str, mode: str = 'r', encoding: str = None):
           filename = filepath.split(os.sep)[-1]
           if filename in mock_files:
               return mocker.mock_open(read_data=mock_files[filename]).return_value
           raise FileNotFoundError

       mocker.patch('os.listdir', mock_listdir)
       mocker.patch('os.path.isfile', mock_isfile)
       mocker.patch('builtins.open', mock_open_func)

       submissions = load_submissions('path/to/submissions')
       assert submissions == mock_files
   ```

## Consequences

### Positive Consequences

- **Flexibility:** The function can handle any submission stored as a text file in the specified directory.
- **Simplicity:** The implementation is straightforward and easy to understand.
- **Testability:** The function is easily testable with mock file systems.

### Negative Consequences

- **Format Dependency:** The function currently assumes that submissions are text files. Handling other formats (e.g., PDFs, code files) would require additional parsing logic.
- **Error Handling:** Additional error handling may be required to manage missing or malformed files in the directory.

## Alternatives Considered

1. **Hardcoding Submissions:**
   - This approach would have been simpler but far less flexible and scalable.

2. **Using a Database:**
   - Storing submissions in a database could provide more structure but would introduce additional complexity and overhead.

## Conclusion

The chosen approach of implementing the `load_submissions` function in `submission_loader.py` provides the necessary flexibility, simplicity, and testability for loading and parsing student submissions in GradeBot Guru. This decision ensures that the application can easily integrate and utilize student submissions for grading and feedback.
