import json
import os
from typing import Dict, Any, Optional

CONFIG_SCHEMA: Dict[str, Any] = {
    'llm_providers': [],
    'number_of_repeats': 1,
    'repeat_each_provider': False,
    'rubric_path': 'path/to/rubric.csv',
    'submission_path': 'path/to/submissions',
    'logging_level': 'INFO'
}


def get_default_config() -> Dict[str, Any]:
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


def load_config(config_file_path: Optional[str] = None) -> Dict[str, Any]:
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
        with open(config_file_path, 'r') as file:
            file_config = json.load(file)
            config.update(file_config)

    # Override with environment variables if they exist
    for key in config.keys():
        env_value = os.getenv(key.upper())
        if env_value:
            if isinstance(config[key], bool):
                config[key] = env_value.lower() in ['true', '1', 'yes']
            elif isinstance(config[key], int):
                config[key] = int(env_value)
            else:
                config[key] = env_value

    return config
