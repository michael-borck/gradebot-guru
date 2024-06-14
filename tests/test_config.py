import os
import json
import pytest
from unittest.mock import patch, mock_open
from gradebotguru.config import load_config, get_default_config


def test_load_default_config():
    config = load_config()
    assert config == get_default_config()


@patch('os.path.exists', return_value=True)
@patch('builtins.open', new_callable=mock_open, read_data='{"llm_provider": "local"}')
def test_load_config_from_file(mock_open, mock_exists):
    config = load_config('path/to/config.json')
    assert config['llm_provider'] == 'local'


@patch.dict(os.environ, {'LLM_PROVIDER': 'local'})
def test_load_config_from_env():
    config = load_config()
    assert config['llm_provider'] == 'local'


@patch('os.path.exists', return_value=True)
@patch('builtins.open', new_callable=mock_open, read_data='{"llm_provider": "local"}')
@patch.dict(os.environ, {'RUBRIC_PATH': 'new/path/to/rubric.csv'})
def test_load_config_file_and_env(mock_open, mock_exists):
    config = load_config('path/to/config.json')
    assert config['llm_provider'] == 'local'
    assert config['rubric_path'] == 'new/path/to/rubric.csv'
