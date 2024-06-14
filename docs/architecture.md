# Architecture

## Overview

GradeBot Guru is designed to automate the evaluation of student submissions using AI-powered grading. This document provides an overview of the system architecture, including key components, their interactions, and data flow within the system.

## Modules

- **`gradebotguru`**: Core application logic.
  - **`main.py`**: Entry point for the CLI application.
  - **`grader.py`**: Core grading logic.
  - **`rubric_loader.py`**: Loading and parsing rubrics.
  - **`submission_loader.py`**: Loading and parsing submissions.
  - **`logging_config.py`**: Logging configuration.
  - **`config.py`**: Configuration settings.
  - **`prompts.py`**: Logic for generating prompts for LLMs.
  - **`response_parser.py`**: Logic for parsing LLM responses.
- **`llm_interface`**: Interaction with LLMs.
  - **`__init__.py`**: Initialization file.
  - **`factory.py`**: Factory to create LLM instances.
  - **`base_llm.py`**: Base class/interface for LLMs.
  - **`openai.py`**: Implementation for OpenAI LLM.
  - **`local_llm.py`**: Implementation for local LLM.

## Data Flow

### Visual Diagram

```plaintext
+--------------------+     +--------------------+
|      main.py       |<----|   config.py        |
+--------+-----------+     +--------------------+
         |
         v
+--------------------+     +--------------------+
|   logging_config.py|<--> |  grader.py         |
+--------------------+     +--------------------+
         |
         v
+--------------------+     +--------------------+
|  rubric_loader.py  |<--> | submission_loader.py|
+--------------------+     +--------------------+
         |
         v
+--------------------+
|    llm_interface/  |
+--------+-----------+
         |
         v
+--------+-----------+
| factory.py         |
| base_llm.py        |
| openai.py          |
| local_llm.py       |
+--------------------+
         |
         v
+--------------------+     +--------------------+
|    prompts.py      |<--> | response_parser.py |
+--------------------+     +--------------------+
```

### Interaction Explanation

- **`main.py`**: Entry point and control flow of the application. Initializes logging, loads configuration, and coordinates grading.
- **`config.py`**: Provides configuration settings for the application.
- **`logging_config.py`**: Sets up logging for the application.
- **`grader.py`**: Core logic for processing submissions. Uses `rubric_loader.py` to load rubrics and `submission_loader.py` to load student submissions.
- **`llm_interface`**: Contains logic to interact with LLMs. `factory.py` creates instances of LLMs using `base_llm.py` as a base class. Specific implementations like `openai.py` and `local_llm.py` provide concrete classes.
- **`prompts.py`**: Generates prompts for LLMs based on submissions and rubrics.
- **`response_parser.py`**: Parses responses from LLMs to extract grades and feedback.

## Design Patterns

### Factory Pattern for `llm_interface`

The factory pattern is used in `llm_interface` to create instances of different LLM classes. This allows the system to be easily extended with new LLM implementations without modifying the core logic.

**Example:**

```python
# factory.py

from llm_interface.base_llm import BaseLLM
from llm_interface.openai import OpenAILLM
from llm_interface.local_llm import LocalLLM

def create_llm(provider_name):
    if provider_name == 'openai':
        return OpenAILLM()
    elif provider_name == 'local':
        return LocalLLM()
    else:
        raise ValueError("Unsupported LLM provider")
```
