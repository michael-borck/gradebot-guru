import argparse
import os
import shutil

import git
import toml


def bump_version(bump_type: str) -> str:
    """
    Bumps the version in pyproject.toml based on the specified bump type.

    Args:
        bump_type (str): The type of version bump ('major', 'minor', 'patch').

    Returns:
        str: The new version.
    """
    with open("pyproject.toml") as file:
        config = toml.load(file)

    version = config["tool"]["poetry"]["version"]
    major, minor, patch = map(int, version.split("."))

    if bump_type == "major":
        major += 1
        minor = 0
        patch = 0
    elif bump_type == "minor":
        minor += 1
        patch = 0
    elif bump_type == "patch":
        patch += 1
    else:
        raise ValueError(f"Unknown bump type: {bump_type}")

    new_version = f"{major}.{minor}.{patch}"
    config["tool"]["poetry"]["version"] = new_version

    with open("pyproject.toml", "w") as file:
        toml.dump(config, file)

    return new_version


def generate_changelog() -> None:
    """
    Generates or updates the changelog file (CHANGELOG.md) with categorized commit messages.
    """
    repo = git.Repo(".")
    tags = sorted(repo.tags, key=lambda t: t.commit.committed_datetime)

    changelog_content = "# Changelog\n\nAll notable changes to this project will be documented in this file.\n\n"
    changelog_content += "The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)\n"
    changelog_content += "and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).\n\n"

    previous_tag: git.TagReference | None = None
    for tag in tags:
        if previous_tag:
            changelog_content += generate_section(repo, previous_tag, tag)
        previous_tag = tag

    changelog_content += generate_section(repo, previous_tag, "HEAD", unreleased=True)

    with open("CHANGELOG.md", "w") as file:
        file.write(changelog_content)


def generate_section(
    repo: git.Repo, from_ref: str, to_ref: str, unreleased: bool = False
) -> str:
    """
    Generates a section of the changelog for the specified range of commits.

    Args:
        repo (git.Repo): The Git repository object.
        from_ref (str): The starting reference (commit hash or tag).
        to_ref (str): The ending reference (commit hash or tag).
        unreleased (bool, optional): Indicates if this section is for unreleased changes. Defaults to False.

    Returns:
        str: The generated changelog section content.
    """
    section_title = (
        "## Unreleased\n"
        if unreleased
        else f"## [{to_ref}] - {to_ref.commit.committed_datetime.date()}\n"
    )
    compare_link = f"<small>[Compare with latest](https://github.com/BARG-Curtin-University/gradebotguru/compare/{from_ref}...{to_ref})</small>\n"
    section_content = f"{section_title}\n{compare_link}\n"

    commits = list(repo.iter_commits(f"{from_ref}..{to_ref}"))
    if not commits:
        section_content += "No notable changes.\n\n"
        return section_content

    categories = {
        "Features": "feat:",
        "Documentation": "docs:",
        "Chores": "chore:",
        "Refactoring": "refactor:",
    }
    categorized_commits = {category: [] for category in categories}

    for commit in commits:
        for category, prefix in categories.items():
            if prefix in commit.message:
                categorized_commits[category].append(commit)
                break

    for category, commits in categorized_commits.items():
        if commits:
            section_content += f"### {category}\n"
            for commit in commits:
                section_content += f"* {commit.message.strip()} ({commit.hexsha[:7]})\n"
            section_content += "\n"

    return section_content


def commit_changes(version: str) -> None:
    """
    Commits the changes (version bump, changelog update, copied files) and tags the new version.

    Args:
        version (str): The new version to tag.
    """
    repo = git.Repo(".")
    repo.git.add("pyproject.toml")
    repo.git.add("CHANGELOG.md")
    repo.git.add("docs/")  # Add any other necessary files or directories
    repo.index.commit(f"chore: bump version to {version} and update changelog")
    repo.create_tag(version)


def copy_files() -> None:
    """
    Copies specific markdown files from the root folder to the docs folder,
    converting the file names to lowercase.
    """
    files_to_copy = ["ROADMAP.md", "CONTRIBUTING.md", "CODE_OF_CONDUCT.md"]
    dest_dir = "docs/"
    os.makedirs(dest_dir, exist_ok=True)

    for file in files_to_copy:
        src_file = file
        dest_file = os.path.join(dest_dir, file.lower())
        shutil.copy(src_file, dest_file)


def push_changes() -> None:
    """
    Pushes the commits and tags to the remote repository.
    """
    repo = git.Repo(".")
    origin = repo.remote(name="origin")

    current_branch = repo.active_branch
    try:
        origin.push()
    except git.exc.GitCommandError as e:
        if "fatal: The current branch" in str(e) and "has no upstream branch" in str(e):
            print(f"Setting upstream for branch {current_branch}")
            origin.push(set_upstream=True)
        else:
            raise e

    origin.push(tags=True)


def main(bump_type: str) -> None:
    """
    Main function to orchestrate the release process.

    Args:
        bump_type (str): The type of version bump ('major', 'minor', 'patch').
    """
    new_version = bump_version(bump_type)
    generate_changelog()
    copy_files()
    commit_changes(new_version)
    push_changes()
    print(f"Released version {new_version}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Automate the release process.")
    parser.add_argument(
        "bump_type",
        choices=["major", "minor", "patch"],
        help="Type of version bump (major, minor, patch)",
    )
    args = parser.parse_args()
    main(args.bump_type)
