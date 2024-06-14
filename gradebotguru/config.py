# config.py

import json
import os

CONFIG_SCHEMA = {
    'llm_provider': 'openai',  # or 'local'
    'rubric_path': 'path/to/rubric.csv',
    'submission_path': 'path/to/submissions',
    'logging_level': 'INFO',  # or 'DEBUG', 'ERROR'
    'other_setting': 'value'
}

def get_default_config():
    return CONFIG_SCHEMA.copy()

def load_config(config_file_path=None):
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
