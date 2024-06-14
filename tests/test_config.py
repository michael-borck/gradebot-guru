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
