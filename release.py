import argparse
import subprocess
import git
import toml
import os
import shutil


def bump_version(bump_type):
    with open('pyproject.toml', 'r') as file:
        config = toml.load(file)

    # Assuming the version follows semantic versioning
    version = config['tool']['poetry']['version']
    major, minor, patch = map(int, version.split('.'))

    if bump_type == 'major':
        major += 1
        minor = 0
        patch = 0
    elif bump_type == 'minor':
        minor += 1
        patch = 0
    elif bump_type == 'patch':
        patch += 1
    else:
        raise ValueError(f"Unknown bump type: {bump_type}")

    new_version = f"{major}.{minor}.{patch}"
    config['tool']['poetry']['version'] = new_version

    with open('pyproject.toml', 'w') as file:
        toml.dump(config, file)

    return new_version


def generate_changelog():
    repo = git.Repo('.')
    tags = sorted(repo.tags, key=lambda t: t.commit.committed_datetime)

    changelog_content = "# Changelog\n\nAll notable changes to this project will be documented in this file.\n\n"
    changelog_content += "The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)\n"
    changelog_content += "and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).\n\n"

    previous_tag = None
    for tag in tags:
        if previous_tag:
            changelog_content += generate_section(repo, previous_tag, tag)
        previous_tag = tag

    # Add unreleased changes
    changelog_content += generate_section(repo, previous_tag, 'HEAD', unreleased=True)

    with open('CHANGELOG.md', 'w') as file:
        file.write(changelog_content)


def generate_section(repo, from_ref, to_ref, unreleased=False):
    section_title = f"## Unreleased\n" if unreleased else f"## [{to_ref}] - {to_ref.commit.committed_datetime.date()}\n"
    compare_link = f"<small>[Compare with latest](https://github.com/BARG-Curtin-University/gradebotguru/compare/{from_ref}...{to_ref})</small>\n"
    section_content = f"{section_title}\n{compare_link}\n"

    commits = list(repo.iter_commits(f"{from_ref}..{to_ref}"))
    if not commits:
        section_content += "No notable changes.\n\n"
        return section_content

    features = [commit for commit in commits if "feat:" in commit.message]
    fixes = [commit for commit in commits if "fix:" in commit.message]
    others = [commit for commit in commits if commit not in features + fixes]

    if features:
        section_content += "### Features\n"
        for commit in features:
            section_content += f"* {commit.message.strip()} ({commit.hexsha[:7]})\n"

    if fixes:
        section_content += "### Fixes\n"
        for commit in fixes:
            section_content += f"* {commit.message.strip()} ({commit.hexsha[:7]})\n"

    if others:
        section_content += "### Others\n"
        for commit in others:
            section_content += f"* {commit.message.strip()} ({commit.hexsha[:7]})\n"

    section_content += "\n"
    return section_content


def commit_changes(version):
    repo = git.Repo('.')
    repo.git.add('pyproject.toml')
    repo.git.add('CHANGELOG.md')
    repo.git.add('docs/')  # Add any other necessary files or directories
    repo.index.commit(f"Bump version to {version} and update changelog")
    repo.create_tag(version)


def copy_files():
    files_to_copy = ['ROADMAP.md', 'CONTRIBUTING.md', 'CODE_OF_CONDUCT.md']
    dest_dir = 'docs/'
    os.makedirs(dest_dir, exist_ok=True)
    for file in files_to_copy:
        shutil.copy(file, dest_dir)


def push_changes():
    repo = git.Repo('.')
    origin = repo.remote(name='origin')

    current_branch = repo.active_branch
    try:
        # Check if the branch has an upstream branch set
        origin.push()
    except git.exc.GitCommandError as e:
        if 'fatal: The current branch' in str(e) and 'has no upstream branch' in str(e):
            print(f"Setting upstream for branch {current_branch}")
            origin.push(set_upstream=True)
        else:
            raise e

    origin.push(tags=True)


def main(bump_type):
    new_version = bump_version(bump_type)
    generate_changelog()
    copy_files()
    commit_changes(new_version)
    push_changes()
    print(f"Released version {new_version}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Automate the release process.')
    parser.add_argument('bump_type', choices=['major', 'minor', 'patch'], help='Type of version bump (major, minor, patch)')
    args = parser.parse_args()
    main(args.bump_type)
