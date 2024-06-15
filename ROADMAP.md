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
   - Implement `prompts.py` to generate well-formatted prompts for the LLM.
   - Write unit tests for prompt generation.

5. **Response Parsing:**
   - Implement `response_parser.py` to extract grades and feedback from the LLM's responses.
   - Write unit tests for response parsing.

6. **Grading Logic:**
   - Implement `grader.py` to orchestrate the grading process (loading rubric, loading submissions, generating prompts, interacting with LLM, parsing responses).
   - Write unit tests for the grading logic.

## Phase 3: Command-Line Interface (CLI)

**Objective:** Develop the CLI for users to interact with the application.

#### Tasks:
1. **CLI Implementation:**
   - Implement `main.py` using `argparse` to handle command-line arguments.
   - Integrate the CLI with the core grading logic.

2. **CLI Testing:**
   - Write tests for the CLI to ensure it handles various user inputs correctly.

## Phase 4: Documentation and Examples

**Objective:** Provide comprehensive documentation and examples to help users get started with the application.

#### Tasks:
1. **User Documentation:**
   - Create a `docs/` folder.
   - Write a setup guide (`setup_guide.md`).
   - Write a user guide (`user_guide.md`).
   - Provide examples of rubrics, submissions, and LLM prompts.

2. **API Documentation:**
   - Generate API documentation using tools like Sphinx or MkDocs.
   - Ensure all public methods and classes are well-documented.

## Phase 5: Testing and Quality Assurance

**Objective:** Ensure the application is robust and reliable through extensive testing and quality assurance.

#### Tasks:
1. **Unit Testing:**
   - Ensure all modules have comprehensive unit tests.
   - Achieve high code coverage.

2. **Integration Testing:**
   - Implement integration tests to verify the end-to-end functionality.
   - Test the entire grading workflow with sample data.

3. **User Acceptance Testing (UAT):**
   - Conduct UAT with a sample group of educators and students.
   - Collect feedback and make necessary improvements.

## Phase 6: Beta Release and Feedback

**Objective:** Release a beta version of the application to a broader audience for feedback and improvements.

#### Tasks:
1. **Beta Release:**
   - Publish the beta version to PyPI.
   - Announce the beta release to potential users (e.g., educators, institutions).

2. **Feedback Collection:**
   - Set up a feedback mechanism (e.g., GitHub issues, surveys).
   - Collect and analyze user feedback.
   - Identify common issues and feature requests.

## Phase 7: Final Release and Post-Release Support

**Objective:** Release the final version of the application and provide ongoing support and improvements.

#### Tasks:
1. **Final Release:**
   - Address issues and improvements identified during the beta phase.
   - Publish the final version to PyPI.
   - Update documentation and examples as needed.

2. **Post-Release Support:**
   - Monitor user feedback and issues.
   - Provide regular updates and bug fixes.
   - Plan for future enhancements and features based on user feedback.

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
