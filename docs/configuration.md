# Configuration

## Configuration Options

- `llm_providers`: List of LLM providers with their respective settings.
- `number_of_repeats`: Number of times to repeat the grading process.
- `repeat_each_provider`: Whether to repeat grading for each provider.
- `aggregation_method`: Method to aggregate grades. Options are `simple_average`, `weighted_average`, `median`, `bias_adjusted`.
- `bias_adjustments`: Bias adjustments for specific providers.
- `rubric_path`: Path to the grading rubric.
- `submission_path`: Path to the student submissions.
- `logging_level`: Logging level.
- `output_format`: Format of the output.
- `output_path`: Path to save the output.
- `output_fields`: Fields to include in the output.
- `llm_prompt_template`: Custom prompt template for LLMs.
- `summarize_feedback`: Whether to summarize feedback from all LLMs.

### Example Configuration

```json
{
    "llm_providers": [
        {"provider": "openai", "api_key": "your_openai_api_key", "model": "text-davinci-003", "temperature": 0.7},
        {"provider": "ollama", "api_key": "your_ollama_api_key", "model": "llama3", "server_url": "http://localhost:11434/v1"}
    ],
    "number_of_repeats": 3,
    "repeat_each_provider": true,
    "aggregation_method": "bias_adjusted",
    "bias_adjustments": {"openai": 5.0, "ollama": 3.0},
    "rubric_path": "path/to/rubric.csv",
    "submission_path": "path/to/submissions",
    "logging_level": "INFO",
    "output_format": "json",
    "output_path": "path/to/output",
    "output_fields": ["student_id", "grade", "feedback", "sentiment", "style"],
    "llm_prompt_template": "Grade the following student submission based on the rubric provided. The rubric is as follows: {rubric}. The student submission is as follows: {submission}.",
    "summarize_feedback": true
}
