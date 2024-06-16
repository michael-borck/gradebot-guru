# ADR 0017: Maintain Change Log with Categorised Commit Messages

## Context and Problem Statement

To ensure clarity and traceability of changes in the project, it is important to maintain a comprehensive change log that categorizes commit messages by their type, such as features, documentation, chores, and refactoring. This helps in understanding the evolution of the project and aids in better project management.

## Decision Drivers

- Need for clear and categorized documentation of changes
- Improved traceability and project management
- Adherence to best practices in software development

## Considered Options

- Manual maintenance of the change log
- Automated change log generation with categorized commit messages

## Decision Outcome

Chosen option: "Automated change log generation with categorized commit messages", because it provides a systematic way to document changes and reduces the overhead of manually updating the change log.

## Consequences

- Positive consequence 1: Improved clarity and traceability of project changes.
- Positive consequence 2: Reduced manual effort in maintaining the change log.
- Negative consequence 1: Initial setup and configuration effort for automation.

## Categories

- **Features** (`feat:`): New features or significant updates to existing features.
- **Documentation** (`docs:`): Updates or additions to documentation.
- **Chores** (`chore:`): Routine tasks, such as version bumps or dependency updates.
- **Refactoring** (`refactor:`): Code changes that neither fix bugs nor add features.
- **Fixes** (`fix:`): Bug fixes.
- **Tests** (`test:`): Adding or updating tests.

## Implementation

- Use a release script to automate the version bumping, changelog generation, and commit tagging.
- Ensure all commit messages follow the defined categories for consistency.

## Examples

```bash
# Example of a feature commit
git commit -m "feat: Add new functionality for handling detached HEAD state"

# Example of a documentation commit
git commit -m "docs: Update README with instructions for fixing detached HEAD state"

# Example of a chore commit
git commit -m "chore: Update dependencies and fix detached HEAD state issue"

# Example of a refactor commit
git commit -m "refactor: Improve code structure for handling detached HEAD state"

# Example of a style commit
git commit -m "style: Format code to meet style guidelines"

# Example of a CI commit
git commit -m "ci: Update CI configuration for better handling of detached HEAD state"

# Example of a revert commit
git commit -m "revert: Revert changes that caused detached HEAD state issue"

# Example of a performance commit
git commit -m "perf: Optimize performance of code handling detached HEAD state"
```