# ADR 0001: Configuration Loader

## Status

Accepted

## Context

GradeBot Guru needs a flexible and robust way to manage configuration settings. These settings include but are not limited to:
- LLM provider (e.g., OpenAI or local)
- Paths to rubric and submission files
- Logging levels

The configuration settings need to be loaded from default values, configuration files, and environment variables, with the ability to override default settings.

## Decision

We will implement a configuration loader in `config.py` that:
1. Defines a default configuration schema.
2. Loads configuration settings from a specified configuration file (if provided).
3. Overrides settings with environment variables (if they exist).
4. Merges all settings to produce the final configuration.

### Implementation

1. **Define the Configuration Schema:**

   We define the configuration schema as a dictionary in `config.py`.

   ```python
   # config.py

   CONFIG_SCHEMA = {
       'llm_provider': 'openai',  # or 'local'
       'rubric_path': 'path/to/rubric.csv',
       'submission_path': 'path/to/submissions',
       'logging_level': 'INFO',  # or 'DEBUG', 'ERROR'
       'other_setting': 'value'
   }

   def get_default_config():
       return CONFIG_SCHEMA.copy()
   ```

2. **Implement the `load_config` Function:**

   The `load_config` function loads the configuration from a file and environment variables.

   ```python
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
   ```

3. **Write Unit Tests for the Configuration Loader:**

   We write unit tests to ensure the configuration loader works correctly.

   ```python
    import os
    import pytest
    from pytest_mock import MockerFixture
    from gradebotguru.config import load_config, get_default_config


    def test_load_default_config() -> None:
        """
        Test that the default configuration is loaded correctly.
        """
        config = load_config()
        assert config == get_default_config()


    def test_load_config_from_file(mocker: MockerFixture) -> None:
        """
        Test that configuration is loaded correctly from a file.
        
        Args:
            mocker (MockerFixture): pytest-mock fixture for patching.
        """
        mocker.patch('os.path.exists', return_value=True)
        mocker.patch('builtins.open', mocker.mock_open(read_data='{"llm_provider": "local"}'))

        config = load_config('path/to/config.json')
        assert config['llm_provider'] == 'local'


    def test_load_config_from_env(mocker: MockerFixture) -> None:
        """
        Test that configuration is loaded correctly from environment variables.
        
        Args:
            mocker (MockerFixture): pytest-mock fixture for patching.
        """
        mocker.patch.dict(os.environ, {'LLM_PROVIDER': 'local'})

        config = load_config()
        assert config['llm_provider'] == 'local'


    def test_load_config_file_and_env(mocker: MockerFixture) -> None:
        """
        Test that configuration is loaded correctly from both a file and environment variables.
        
        Args:
            mocker (MockerFixture): pytest-mock fixture for patching.
        """
        mocker.patch('os.path.exists', return_value=True)
        mocker.patch('builtins.open', mocker.mock_open(read_data='{"llm_provider": "local"}'))
        mocker.patch.dict(os.environ, {'RUBRIC_PATH': 'new/path/to/rubric.csv'})

        config = load_config('path/to/config.json')
        assert config['llm_provider'] == 'local'
        assert config['rubric_path'] == 'new/path/to/rubric.csv'
   ```

## Consequences

### Positive Consequences

- **Flexibility:** The configuration loader can load settings from multiple sources and override them as needed.
- **Robustness:** By defining a default schema and merging settings from different sources, we ensure that the configuration is always complete and consistent.
- **Testability:** Unit tests can verify that the configuration loader behaves as expected under various conditions.

### Negative Consequences

- **Complexity:** Introducing multiple sources for configuration settings adds some complexity to the configuration management process.
- **Maintenance:** Ensuring that all sources of configuration are properly managed and updated requires ongoing maintenance.

## Alternatives Considered

1. **Hardcoding Configuration Settings:**
   - This approach would have been simpler but far less flexible and scalable.
   
2. **Using a Single Configuration Source:**
   - Relying solely on a configuration file or environment variables would limit flexibility and adaptability to different environments.

## Conclusion

The chosen approach of implementing a configuration loader that merges settings from default values, configuration files, and environment variables provides the necessary flexibility, robustness, and testability for GradeBot Guru. This decision ensures that the application can be easily configured and adapted to different environments and requirements.
