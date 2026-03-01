# GradeBot Guru: Your AI Grading Assistant 👨‍🏫🤖

<!-- BADGES:START -->
[![edtech](https://img.shields.io/badge/-edtech-4caf50?style=flat-square)](https://github.com/topics/edtech) [![artificial-intelligence](https://img.shields.io/badge/-artificial--intelligence-blue?style=flat-square)](https://github.com/topics/artificial-intelligence) [![automated-grading](https://img.shields.io/badge/-automated--grading-blue?style=flat-square)](https://github.com/topics/automated-grading) [![cli-tool](https://img.shields.io/badge/-cli--tool-blue?style=flat-square)](https://github.com/topics/cli-tool) [![education](https://img.shields.io/badge/-education-blue?style=flat-square)](https://github.com/topics/education) [![feedback](https://img.shields.io/badge/-feedback-blue?style=flat-square)](https://github.com/topics/feedback) [![grading](https://img.shields.io/badge/-grading-blue?style=flat-square)](https://github.com/topics/grading) [![llm](https://img.shields.io/badge/-llm-ff6f00?style=flat-square)](https://github.com/topics/llm) [![python](https://img.shields.io/badge/-python-3776ab?style=flat-square)](https://github.com/topics/python) [![tool](https://img.shields.io/badge/-tool-607d8b?style=flat-square)](https://github.com/topics/tool)
<!-- BADGES:END -->

[![PyPI Version](https://img.shields.io/pypi/v/gradebot-guru?color=blue)](https://pypi.org/project/gradebot-guru/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

GradeBot Guru is your friendly AI-powered grading assistant, designed to automate the evaluation of student submissions and provide fast, accurate, and insightful feedback.

## Table of Contents

- [GradeBot Guru: Your AI Grading Assistant 👨‍🏫🤖](#gradebot-guru-your-ai-grading-assistant-)
  - [Table of Contents](#table-of-contents)
  - [Features ✨](#features-)
  - [Installation 🛠️](#installation-️)
  - [Usage 🚀](#usage-)
  - [Configuration ⚙️](#configuration-️)
  - [Examples 📚](#examples-)
  - [Development 👩‍💻](#development-)
  - [Contributing 🙌](#contributing-)
  - [License 📄](#license-)
  - [Contact 📬](#contact-)
  - [Additional Resources](#additional-resources)

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

2. **Install from Source (Development Setup):**

   ```bash
   git clone https://github.com/teaching-repositories/gradebot-guru.git
   cd gradebot-guru
   uv sync --all-extras --dev
   ```

## Usage 🚀

```bash
gradebot-guru --config <config_path> --submissions <submissions_dir>
```

* `<config_path>`: Path to the configuration file (JSON format with LLM settings and rubric path).
* `<submissions_dir>`: The path to the directory containing student submissions (e.g., essays, code).

## Configuration ⚙️

* **LLM Provider:** Set your preferred LLM provider in the configuration file (`config.py`). Currently supports Gemini.

## Examples 📚

```bash
# Basic usage with demo configuration
gradebot-guru --config demo/config.json --submissions demo/text-submissions

# Using custom configuration
gradebot-guru --config my-config.json --submissions ./student-essays
```

## Development 👩‍💻

1. **Running Tests:**

   ```bash
   uv run pytest
   ```

2. **Code Formatting and Linting:**

   ```bash
   uv run ruff format .
   uv run ruff check .
   ```

3. **Type Checking:**

   ```bash
   uv run mypy .
   ```

4. **Building Documentation:**

   ```bash
   uv run mkdocs serve
   ```

## Contributing 🙌

Contributions are welcome! Please see the [Contributing Guidelines](CONTRIBUTING.md) for more details.

## License 📄

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact 📬

For questions or feedback, please contact Michael Borck at [michael@borck.me](mailto:michael@borck.me).

## Additional Resources

- [Project Homepage](http://yourhomepage.com)
- [Documentation](https://teaching-repositories.github.io/gradebot-guru/)
- [Repository](https://github.com/teaching-repositories/gradebot-guru)