### Admin Scripts: Release

## Using the Release Script

The `release.py` script automates the release process, including version bumping, changelog generation, and pushing changes to the remote repository.

### Command-Line Arguments

- **bump_type**: The type of version bump. Can be 'major', 'minor', or 'patch'.

### Example Usage

```bash
poetry run python release.py patch
poetry run python release.py minor
poetry run python release.py major
```
