import json
import os
from typing import Any

CONFIG_SCHEMA: dict[str, Any] = {
    "llm_providers": [
        {
            "provider": "openai",
            "api_key": "your_openai_api_key",
            "model": "gpt-3-turbo",
            "temperature": 0.7,
        }
    ],
    "number_of_repeats": 1,
    "repeat_each_provider": False,
    "aggregation_method": "simple_average",
    "bias_adjustments": {},
    "rubric_path": "path/to/rubric.csv",
    "submission_path": "path/to/submissions",
    "logging_level": "INFO",
    "output_format": "json",
    "output_path": "path/to/output",
    "output_fields": ["student_id", "grade", "feedback", "sentiment", "style"],
    "llm_prompt_template": "Grade the following student submission based on the rubric provided. The rubric is as follows: {rubric}. The student submission is as follows: {submission}.",
}


def get_default_config() -> dict[str, Any]:
    """
    Get the default configuration settings.

    Returns:
        Dict[str, Any]: A copy of the default configuration schema.

    Examples:
        >>> config = get_default_config()
        >>> config['llm_providers']
        []
        >>> config['number_of_repeats']
        1
        >>> config['repeat_each_provider']
        False
        >>> config['rubric_path']
        'path/to/rubric.csv'
        >>> config['submission_path']
        'path/to/submissions'
        >>> config['logging_level']
        'INFO'
    """
    return CONFIG_SCHEMA.copy()


def load_config(config_file_path: str | None = None) -> dict[str, Any]:
    """
    Load the configuration settings, merging defaults with settings from a file
    and environment variables.

    Args:
        config_file_path (Optional[str]): Path to the configuration file. Defaults to None.

    Returns:
        Dict[str, Any]: The final configuration settings.

    Examples:
        >>> default_config = get_default_config()
        >>> config = load_config()
        >>> config == default_config
        True
        >>> mock_config_content = '''
        ... {
        ...     "llm_providers": [
        ...         {"provider": "openai", "api_key": "mock_key", "model": "text-davinci-003"}
        ...     ],
        ...     "number_of_repeats": 3,
        ...     "repeat_each_provider": true,
        ...     "rubric_path": "custom/rubric.csv",
        ...     "submission_path": "custom/submissions",
        ...     "logging_level": "DEBUG"
        ... }
        ... '''
        >>> with open('test_config.json', 'w') as f:
        ...     _ = f.write(mock_config_content)
        >>> config = load_config('test_config.json')
        >>> config['llm_providers']
        [{'provider': 'openai', 'api_key': 'mock_key', 'model': 'text-davinci-003'}]
        >>> config['number_of_repeats']
        3
        >>> config['repeat_each_provider']
        True
        >>> config['rubric_path']
        'custom/rubric.csv'
        >>> config['submission_path']
        'custom/submissions'
        >>> config['logging_level']
        'DEBUG'
        >>> import os; os.remove('test_config.json')
    """
    config = get_default_config()

    # Load from a configuration file if provided
    if config_file_path and os.path.exists(config_file_path):
        with open(config_file_path) as file:
            file_config = json.load(file)
            config.update(file_config)

    # Override with environment variables if they exist
    for key in config.keys():
        env_value = os.getenv(key.upper())
        if env_value:
            config[key] = env_value

    return config
