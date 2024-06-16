import os
import json
import pytest
from pytest_mock import MockerFixture
from gradebotguru.config import load_config, get_default_config


def test_get_default_config() -> None:
    """
    Test getting the default configuration.

    This test verifies that the default configuration settings
    are correctly returned.
    """
    config = get_default_config()
    assert config['llm_providers'] == []
    assert config['number_of_repeats'] == 1
    assert config['repeat_each_provider'] is False
    assert config['rubric_path'] == 'path/to/rubric.csv'
    assert config['submission_path'] == 'path/to/submissions'
    assert config['logging_level'] == 'INFO'


def test_load_config_defaults() -> None:
    """
    Test loading the default configuration.

    This test verifies that the default configuration settings
    are returned when no configuration file is provided.
    """
    config = load_config()
    default_config = get_default_config()
    assert config == default_config


def test_load_config_file(mocker: MockerFixture) -> None:
    """
    Test loading configuration from a file.

    This test verifies that configuration settings from a file are
    correctly loaded and override the default settings.
    """
    mock_config_content = {
        "llm_providers": [
            {"provider": "openai", "api_key": "mock_key", "model": "text-davinci-003"}
        ],
        "number_of_repeats": 3,
        "repeat_each_provider": True,
        "rubric_path": "custom/rubric.csv",
        "submission_path": "custom/submissions",
        "logging_level": "DEBUG"
    }

    # Mock the open function within the load_config context
    mock_open = mocker.patch('builtins.open', mocker.mock_open(read_data=json.dumps(mock_config_content)))
    mocker.patch('os.path.exists', return_value=True)

    config = load_config('path/to/config.json')
    mock_open.assert_called_once_with('path/to/config.json', 'r')

    assert config['llm_providers'] == [{"provider": "openai", "api_key": "mock_key", "model": "text-davinci-003"}]
    assert config['number_of_repeats'] == 3
    assert config['repeat_each_provider'] is True
    assert config['rubric_path'] == 'custom/rubric.csv'
    assert config['submission_path'] == 'custom/submissions'
    assert config['logging_level'] == 'DEBUG'


def test_load_config_env_vars(mocker: MockerFixture) -> None:
    """
    Test loading configuration with environment variables.

    This test verifies that environment variables correctly override
    both the default settings and settings from a configuration file.
    """
    mock_config_content = {
        "llm_providers": [
            {"provider": "openai", "api_key": "mock_key", "model": "text-davinci-003"}
        ],
        "number_of_repeats": 3,
        "repeat_each_provider": True,
        "rubric_path": "custom/rubric.csv",
        "submission_path": "custom/submissions",
        "logging_level": "DEBUG"
    }

    mocker.patch('builtins.open', mocker.mock_open(read_data=json.dumps(mock_config_content)))
    mocker.patch('os.path.exists', return_value=True)
    mocker.patch.dict(os.environ, {"NUMBER_OF_REPEATS": "5", "REPEAT_EACH_PROVIDER": "False"})

    config = load_config('path/to/config.json')
    assert config['number_of_repeats'] == 5
    assert config['repeat_each_provider'] is False
