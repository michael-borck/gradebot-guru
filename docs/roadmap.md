# Roadmap

## Phase 1: Project Initialization and Setup

**Objective:** Establish the foundation of the project with initial setup, tooling, and basic functionality.

#### Tasks:
1. **Repository Setup:**
   - ~~Create a GitHub repository.~~
   - ~~Initialize the project with Poetry.~~
   - ~~Set up the basic folder structure.~~

2. **CI/CD Pipeline:**
   - ~~Configure GitHub Actions for automated testing, building, and publishing.~~
   - ~~Set up secrets for PyPI in the GitHub repository.~~

3. **Initial Commit:**
   - ~~Add a `README.md` with an overview of the project.~~
   - ~~Add `LICENSE` (e.g., MIT License).~~
   - ~~Commit the initial project structure and configurations.~~

## Phase 2: Core Functionality Development

**Objective:** Implement the core features of the GradeBot Guru application, including rubric loading, submission processing, and interaction with the LLM.

#### Tasks:
1. **Rubric Loader:**
   - ~~Implement `rubric_loader.py` to load and parse grading rubrics from CSV and JSON files.~~
   - ~~Write unit tests for rubric loading.~~

2. **Submission Loader:**
   - ~~Implement `submission_loader.py` to load and parse student submissions from various file formats.~~
   - ~~Write unit tests for submission loading.~~

3. **LLM Interface:**
   - ~~Implement the `llm_interface` module using the factory pattern.~~
   - ~~Create a base class (`base_llm.py`) and specific implementations (`gemini.py`, `local_llm.py`).~~
   - ~~Write unit tests for LLM interactions.~~

4. **Prompt Generation:**
   - ~~Implement `prompts.py` to generate well-formatted prompts for the LLM.~~
   - ~~Write unit tests for prompt generation.~~

5. **Response Parsing:**
   - ~~Implement `response_parser.py` to extract grades and feedback from the LLM's responses.~~
   - ~~Write unit tests for response parsing.~~

6. **Grading Logic:**
   - ~~Implement `grader.py` to orchestrate the grading process (loading rubric, loading submissions, generating prompts, interacting with LLM, parsing responses).~~
   - ~~Write unit tests for the grading logic.~~

## Phase 3: Command-Line Interface (CLI)

**Objective:** Develop the CLI for users to interact with the application.

#### Tasks:
1. **CLI Implementation:**
   - ~~Implement `main.py` using `argparse` to handle command-line arguments.~~
   - ~~Integrate the CLI with the core grading logic.~~

2. **CLI Testing:**
   - ~~Write tests for the CLI to ensure it handles various user inputs correctly.~~

## Phase 4: Documentation and Examples

**Objective:** Provide comprehensive documentation and examples to help users get started with the application.

#### Tasks:
1. **User Documentation:**
   - ~~Create a `docs/` folder.~~
   - ~~Write a setup guide (`setup_guide.md`).~~
   - ~~Write a user guide (`user_guide.md`).~~
   - ~~Provide examples of rubrics, submissions, and LLM prompts.~~

2. **API Documentation:**
   - ~~Generate API documentation using tools like Sphinx or MkDocs.~~
   - ~~Ensure all public methods and classes are well-documented.~~

## Phase 5: Testing and Quality Assurance

**Objective:** Ensure the application is robust and reliable through extensive testing and quality assurance.

#### Tasks:
1. **Unit Testing:**
   - ~~Ensure all modules have comprehensive unit tests.~~
   - ~~Achieve high code coverage.~~

2. **Integration Testing:**
   - ~~Implement integration tests to verify the end-to-end functionality.~~
   - ~~Test the entire grading workflow with sample data.~~

3. **User Acceptance Testing (UAT):**
   - Conduct UAT with a sample group of educators and students.
   - Collect feedback and make necessary improvements.

## Phase 6: Local LLM Support

**Objective:** Implement support for local LLM providers to allow cost-effective testing and proof-of-concept validations.

#### Tasks:
1. **Local LLM Integration:**
   - ~~Update `llm_interface.factory` to handle local LLMs.~~
   - ~~Create the `LocalLLM` class to interact with the Ollama server.~~
   - ~~Write unit tests for Local LLM support.~~

2. **Configuration and CLI Enhancements:**
   - Expand the `config.json` to include more configurable parameters.
   - Add CLI commands for `/add`, `/exit`, `/model`, `/provider`, `/config`, etc.

## Phase 7: Critique and Moderation

**Objective:** Enhance the grading process by adding a critique and moderation step using a second LLM.

#### Tasks:
1. **Critique Functionality:**
   - Implement a second LLM to critique the feedback from the first LLM and potentially update the grade.
   - Write unit tests for critique functionality.

## Phase 8: Multiple Submissions and Expert Markers

**Objective:** Implement functionality to submit a submission multiple times and take the average of the grades.

#### Tasks:
1. **Multiple Panel of Markings:**
   - Update grading logic to handle multiple grading rounds.
   - Allow configuration of multiple expert markers.
   - Write unit tests for multiple submissions and expert markers.

## Phase 9: Handle Multiple File Submissions

**Objective:** Implement functionality to handle ZIP files and folders in the submissions directory.

#### Tasks:
1. **Multiple File Submissions:**
   - Implement functionality to handle ZIP files.
   - Implement functionality to handle folders.
   - Write unit tests for multiple file submissions.

## Phase 10: Develop GUI Interface

**Objective:** Create a simple GUI with Tkinter that includes a JSON editor for configuration.

#### Tasks:
1. **GUI Development:**
   - Create a simple GUI with Tkinter.
   - Add buttons to run the CLI version.
   - Implement basic file browsing functionality.
   - Implement functionality to display grading results.

## Phase 11: Additional Features and Refinements

**Objective:** Add more output formats, customization options, and enhance the application.

#### Tasks:
1. **Additional Features:**
   - Add more output formats (e.g., CSV, PDF).
   - Allow customization of output fields and formats.
   - Add custom prompts functionality.
   - Write unit tests for new features and refinements.

## Future Enhancements

**Objective:** Continuously improve the application by adding new features and enhancements.

#### Potential Enhancements:
1. **Web Interface:**
   - Develop a web-based interface using FastAPI and React for a more user-friendly experience.

2. **Integration with LMS:**
   - Integrate with popular Learning Management Systems (e.g., Moodle, Canvas).

3. **Advanced Analytics:**
   - Add features for detailed analytics and reporting on student performance.

4. **Customizable Feedback Templates:**
   - Allow users to create and use custom feedback templates.

5. **Support for Additional LLMs:**
   - Extend the `llm_interface` to support additional LLMs.
