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


def create_issue(issue: Dict[str, Any], headers: Dict[str, str], repo_owner: str, repo_name: str) -> None:
    """
    Create an issue in the specified GitHub repository.

    Args:
        issue (Dict[str, Any]): The issue data to create.
        headers (Dict[str, str]): The headers for the GitHub API request.
        repo_owner (str): The GitHub repository owner.
        repo_name (str): The GitHub repository name.
    """
    url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/issues'
    response = requests.post(url, headers=headers, json=issue)
    if response.status_code == 201:
        print(f'Successfully created issue: {issue["title"]}')
    else:
        print(f'Error creating issue: {issue["title"]}, Status Code: {response.status_code}, Response: {response.json()}')


def main(config_file_path: Optional[str], issues_file_path: str) -> None:
    """
    Main function to upload issues to GitHub from a JSON file.

    Args:
        config_file_path (Optional[str]): Path to the configuration file.
        issues_file_path (str): Path to the JSON file containing issues.
    """
    config = load_config(config_file_path)

    github_token = config['GITHUB_TOKEN']
    repo_owner = config['REPO_OWNER']
    repo_name = config['REPO_NAME']

    # Load issues from JSON file
    with open(issues_file_path) as f:
        issues = json.load(f)

    # Create headers for authentication
    headers = {
        'Authorization': f'token {github_token}',
        'Accept': 'application/vnd.github.v3+json'
    }

    # Iterate through issues and create them
    for issue in issues:
        create_issue(issue, headers, repo_owner, repo_name)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Upload issues to GitHub from a JSON file.')
    parser.add_argument('--config', type=str, default=None, help='Path to the configuration file.')
    parser.add_argument('--issues', type=str, required=True, help='Path to the JSON file containing issues.')
    args = parser.parse_args()

    main(args.config, args.issues)
