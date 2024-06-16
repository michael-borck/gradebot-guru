import requests
import json
import os
import argparse
from typing import Dict, Any, Optional

# Configuration
CONFIG_SCHEMA: Dict[str, Any] = {
    "GITHUB_TOKEN": "add-your-token-here",
    "REPO_OWNER": "add-owner-here",
    "REPO_NAME": "add-repo-name-here",
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


def create_issue(issue: Dict[str, Any], repo_owner: str, repo_name: str, headers: Dict[str, str]) -> None:
    """
    Create an issue on GitHub.

    Args:
        issue (Dict[str, Any]): The issue data to create on GitHub.
        repo_owner (str): The owner of the repository.
        repo_name (str): The name of the repository.
        headers (Dict[str, str]): The headers for the GitHub API request.
    """
    url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/issues'
    response = requests.post(url, headers=headers, json=issue)
    if response.status_code == 201:
        print(f'Successfully created issue: {issue["title"]}')
    else:
        print(f'Error creating issue: {issue["title"]}, Status Code: {response.status_code}, Response: {response.json()}')


def main(config_path: Optional[str] = None):
    """
    Main function to load issues from a JSON file and create them on GitHub.

    Args:
        config_path (Optional[str]): Path to the configuration file. Defaults to None.
    """
    # Load the configuration
    config = load_config(config_path)

    github_token = config["GITHUB_TOKEN"]
    repo_owner = config["REPO_OWNER"]
    repo_name = config["REPO_NAME"]

    # Load issues from JSON file
    with open('scripts/issues.json') as f:
        issues = json.load(f)

    # Create headers for authentication
    headers = {
        'Authorization': f'token {github_token}',
        'Accept': 'application/vnd.github.v3+json'
    }

    # Iterate through issues and create them
    for issue in issues:
        create_issue(issue, repo_owner, repo_name, headers)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Upload issues to GitHub from a JSON file.')
    parser.add_argument('--config', type=str, help='Path to the configuration file')
    args = parser.parse_args()

    main(config_path=args.config)
