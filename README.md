# GradeBot Guru: Your AI Grading Assistant ��‍♂️🤖

[![PyPI Version](https://img.shields.io/pypi/v/gradebot-guru?color=blue)](https://pypi.org/project/gradebot-guru/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

GradeBot Guru is your friendly AI-powered grading assistant, designed to automate the evaluation of student submissions and provide fast, accurate, and insightful feedback.

## Features ✨

* **Automated Grading:**  Quickly and consistently grade student work based on a provided rubric.
* **Detailed Feedback:** Generate personalized feedback highlighting strengths and areas for improvement.
* **Configurable LLM:** Choose your preferred Large Language Model (LLM) provider (e.g., Gemini).
* **Easy-to-Use CLI:**  Simple and intuitive command-line interface for seamless integration into your workflow.

## Installation 🛠️

1. **Install from PyPI:**

   ```bash
   pip install gradebot-guru
   ```

## Usage 🚀

```bash
gradebot-guru <submissions_dir> --rubric <rubric_path>
```

* `<submissions_dir>`: The path to the directory containing student submissions (e.g., essays, code).
* `<rubric_path>`: The path to the grading rubric file (e.g., CSV, JSON).

## Configuration ⚙️

* **LLM Provider:** Set your preferred LLM provider in the configuration file (`config.py`). Currently supports Gemini.

## Examples 📚

```bash
gradebot-guru assignments/ --rubric rubrics/essay_rubric.csv
```

## Contributing 🙌

Contributions are welcome! Please feel free to open issues or submit pull requests.

## License 📄

This project is licensed under the MIT License. See the `LICENSE` file for details.
