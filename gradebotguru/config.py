import json
import os
from typing import Dict, Any, Optional

CONFIG_SCHEMA: Dict[str, Any] = {
    'llm_provider': 'openai',  # or 'local'
    'rubric_path': 'path/to/rubric.csv',
    'submission_path': 'path/to/submissions',
    'logging_level': 'INFO',  # or 'DEBUG', 'ERROR'
    'other_setting': 'value'
}

def get_default_config() -> Dict[str, Any]:
    """
    Get the default configuration settings.

    Returns:
        Dict[str, Any]: A copy of the default configuration schema.

    Examples:
        >>> config = get_default_config()
        >>> config['llm_provider']
        'openai'
        >>> config['rubric_path']
        'path/to/rubric.csv'
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
        >>> with open('test_config.json', 'w') as f:
        ...     json.dump({"llm_provider": "local", "new_setting": "new_value"}, f)
        >>> config = load_config('test_config.json')
        >>> config['llm_provider']
        'local'
        >>> config['new_setting']
        'new_value'
        >>> os.remove('test_config.json')
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
            config[key] = env_value

    return config
