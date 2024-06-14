Sure! Here's the Architectural Decision Record (ADR) for the `load_rubric` function.

# ADR 0003: Load Rubric

## Status

Accepted

## Context

GradeBot Guru requires a mechanism to load and parse grading rubrics that define the criteria and weights used to evaluate student submissions. These rubrics are typically stored in a CSV format and need to be loaded into the application to guide the grading process.

## Decision

We will implement a function named `load_rubric` in `rubric_loader.py` that:
1. Loads the rubric from a CSV file.
2. Parses the rubric into a dictionary format where the keys are the criteria and the values are the weights.

### Implementation

1. **Define the Rubric Schema:**

   The rubric will be stored in a CSV file with two columns: `criterion` and `weight`.

   ```csv
   criterion,weight
   content,0.4
   structure,0.3
   grammar,0.3
   ```

2. **Implement the `load_rubric` Function:**

   The `load_rubric` function will read the CSV file and parse its contents into a dictionary.

   ```python
   # rubric_loader.py

   import csv
   from typing import Dict

   def load_rubric(file_path: str) -> Dict[str, float]:
       """
       Load and parse a grading rubric from a CSV file.

       Args:
           file_path (str): Path to the CSV file containing the rubric.

       Returns:
           Dict[str, float]: A dictionary where keys are criteria and values are weights.
       """
       rubric = {}
       with open(file_path, mode='r', encoding='utf-8') as file:
           reader = csv.DictReader(file)
           for row in reader:
               criterion = row['criterion']
               weight = float(row['weight'])
               rubric[criterion] = weight
       return rubric
   ```

3. **Write Unit Tests for the Rubric Loader:**

   We will write unit tests to ensure the `load_rubric` function works correctly.

   ```python
   # tests/test_rubric_loader.py

   import pytest
   from pytest_mock import MockerFixture
   from gradebotguru.rubric_loader import load_rubric

   def test_load_rubric(mocker: MockerFixture) -> None:
       """
       Test loading and parsing a rubric from a CSV file.

       Mocks the presence of a CSV file and checks if `load_rubric`
       correctly reads and parses the file.
       """
       mock_csv_content = "criterion,weight\ncontent,0.4\nstructure,0.3\ngrammar,0.3\n"
       mocker.patch('builtins.open', mocker.mock_open(read_data=mock_csv_content))

       rubric = load_rubric('path/to/rubric.csv')
       expected_rubric = {
           'content': 0.4,
           'structure': 0.3,
           'grammar': 0.3
       }
       assert rubric == expected_rubric
   ```

## Consequences

### Positive Consequences

- **Flexibility:** The function can handle any rubric stored in the defined CSV format.
- **Simplicity:** The implementation is straightforward and easy to understand.
- **Testability:** The function is easily testable with mock CSV files.

### Negative Consequences

- **Format Dependency:** The function relies on the rubric being in a specific CSV format. Any deviation from this format will cause errors.
- **Error Handling:** Additional error handling may be required to manage missing or malformed data in the CSV file.

## Alternatives Considered

1. **Hardcoding Rubric Values:**
   - This approach would have been simpler but far less flexible and scalable.

2. **Using a Different File Format (e.g., JSON, XML):**
   - JSON or XML could provide more structure but would be less user-friendly for educators who are used to working with spreadsheets.

## Conclusion

The chosen approach of implementing the `load_rubric` function in `rubric_loader.py` to load and parse grading rubrics from a CSV file provides the necessary flexibility, simplicity, and testability for GradeBot Guru. This decision ensures that the application can easily integrate and utilize grading rubrics to guide the evaluation process.
