### Admin Script: Upload Issues form JOSN

## Configuration Instructions

### Environment Variables

- **GITHUB_TOKEN**: Your GitHub token should be specified as an environment variable. It is not included in the config.json file for security reasons.

### Config.json Structure

- **REPO_OWNER**: The owner of the GitHub repository.
- **REPO_NAME**: The name of the GitHub repository.
- **INSTRUCTIONS**: Additional instructions or notes (this is not used by the script).

Example `config.json`:
```json
{
    "REPO_OWNER": "add-owner-here",
    "REPO_NAME": "add-repo-name-here",
    "INSTRUCTIONS": "Set the GITHUB_TOKEN environment variable to your GitHub token."
}
```

## Using the Upload Issues Script

The `upload_issues_from_json.py` script allows you to bulk upload issues to your GitHub repository.

### Command-Line Arguments

- **--config**: Path to the configuration file. If not provided, it defaults to `config.json`.
- **--issues**: Path to the JSON file containing the issues. If not provided, it defaults to `issues.json`.

### Example Usage

```bash
python upload_issues_from_json.py --config path/to/config.json --issues path/to/issues.json
```
