# ADR 0009: Build Process and Release Automation

## Status
Accepted

## Context
We need an automated and consistent process for bumping versions, generating changelogs, and handling releases for the GradeBot Guru project. Initially, standard-version (a Node.js tool) was considered, but adding Node.js dependencies to a Python project was deemed suboptimal.

## Decision
We decided to implement a custom Python script (`release.py`) to handle the build and release process. This script:
- Bumps the version in `pyproject.toml`.
- Generates or updates the `CHANGELOG.md` based on commit messages.
- Copies important documentation files to the `docs` directory.
- Commits the changes and tags the new version.
- Pushes the changes and tags to the remote repository.

## Consequences
- The build process remains within the Python ecosystem, reducing the complexity of dependencies.
- The release process is automated, reducing the likelihood of human error.
- Contributors can easily understand and modify the release process as needed.

## Implementation
The `release.py` script is used for automating the release process. Dependencies for this script are included in `pyproject.toml`.

### Script Overview

```python
# (Include the full release.py script here)
```

## Usage
Run the following command to automate the release process:

```sh
python release.py <bump_type>
```

Where `<bump_type>` can be `major`, `minor`, or `patch`.

---

```

### Documentation for GitHub Project Board

#### `docs/project-management.md`

```markdown
# Project Management

## Overview
This document outlines the project management practices used for the GradeBot Guru project, including the use of GitHub project boards and links to relevant issues.

## GitHub Project Board
We use GitHub Project Boards to manage and track the progress of tasks, issues, and features. The board is organized into columns representing different stages of the workflow, such as "To Do", "In Progress", and "Done".

### Project Board
You can access the GitHub project board [here](https://github.com/your-repo/your-project/projects).

## Issues
Issues are used to track tasks, bugs, and feature requests. Each issue is linked to the project board for better visibility and tracking.

### Creating Issues
- Use the provided issue templates to create new issues.
- Assign the issue to the appropriate column in the project board.

### Example Issues
- [Issue 1: Implement Configuration Loader](https://github.com/your-repo/your-project/issues/1)
- [Issue 2: Setup Logging Configuration](https://github.com/your-repo/your-project/issues/2)
