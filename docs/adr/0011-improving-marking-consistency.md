# ADR 0011: Improving Marking Consistency

## Status
Accepted

## Context
Ensuring marking consistency in AI-powered grading systems is a critical challenge. While prompt engineering provides a foundation, there are several other strategies that can be employed to enhance consistency, accuracy, and reliability in grading different types of assessments (essays, code, webpages, videos, etc.).

## Decision
We will adopt a multi-faceted approach to improve marking consistency by leveraging the following strategies:

### 1. Prompt Engineering
- **Using Structured Templates:** Define clear and consistent templates for different types of assessments.
- **Including Detailed Instructions:** Add specific criteria and examples in the prompts to minimize ambiguity.

### 2. Response Augmentation and Analysis
- **Chain of Thought Prompting:** Encourage the model to think step-by-step by explicitly asking it to explain its reasoning process.
- **Self-Consistency Decoding:** Generate multiple outputs and use an ensemble approach to determine the most consistent response.

### 3. Retrieval-Augmented Generation (RAG)
- **RAG Integration:** Integrate RAG to pull in relevant information or previous similar evaluations to improve consistency.
- **Contextual Retrieval:** Fetch relevant sections from documentation, rubrics, or previous feedback to inform the current evaluation.

### 4. Fine-Tuning
- **Domain-Specific Fine-Tuning:** Fine-tune a model on a dataset specific to the type of assessments to improve performance and consistency.
- **Incremental Fine-Tuning:** Collect data from ongoing assessments to incrementally fine-tune the model, enhancing its accuracy over time.

### 5. Hybrid Approaches
- **Human-in-the-Loop:** Use human graders to review and correct AI evaluations initially to build a high-quality dataset for fine-tuning.
- **Rubric-Based Systems:** Implement rule-based systems that work alongside the AI to ensure baseline consistency by checking for specific criteria.

### 6. Continuous Improvement and Monitoring
- **Regular Reviews and Updates:** Continuously monitor AI performance, collect user feedback, and iteratively improve the system.
- **Benchmarking and Testing:** Regularly test the system with benchmark datasets to ensure it meets consistency and accuracy standards.

### 7. Multi-Modal Assessment
- **Multi-Modal Models:** Develop or utilize models that can handle different types of inputs (text, code, video, etc.) in an integrated manner to maintain consistency across various assessment types.

### 8. Standardized Feedback Templates
- **Customizable Feedback Templates:** Allow educators to create and use customizable feedback templates for consistent structured feedback, while still allowing for personalized comments.

## Consequences
### Positive
- Improved consistency and reliability in AI-assisted grading.
- Enhanced ability to handle different types of assessments.
- Incremental improvements based on real-world usage and feedback.

### Negative
- Initial setup and integration of these strategies will require additional time and resources.
- Continuous monitoring and updates are necessary to maintain performance.

## Next Steps
- Implement structured templates and detailed instructions for prompt engineering.
- Integrate response augmentation techniques such as chain of thought prompting and self-consistency decoding.
- Explore the use of RAG for context retrieval.
- Start collecting data for domain-specific and incremental fine-tuning.
- Set up human-in-the-loop processes and rule-based systems for initial reviews.
- Establish a continuous improvement and monitoring framework.
- Develop or utilize multi-modal models for diverse assessment types.
- Create and implement standardized feedback templates for consistent feedback.

