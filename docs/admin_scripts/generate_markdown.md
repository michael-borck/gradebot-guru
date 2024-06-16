# Generate Markdown Script

## Purpose

The `generate_markdown.py` script is designed to automate the creation of Markdown files that include `mkdocstrings` directives for Python files. This is useful for generating documentation for a Python project, allowing you to easily include documentation for all Python modules and scripts in your project's documentation site.

## Usage

### Command Line Arguments

The script accepts two optional command line arguments:

- `--input_dir`: The directory containing the Python files for which you want to generate Markdown documentation. Defaults to the current directory (`.`) if not specified.
- `--output_dir`: The directory where the generated Markdown files will be saved. Defaults to the current directory (`.`) if not specified.

### Running the Script

To run the script, use the following command:

```bash
python generate_markdown.py --input_dir path/to/input --output_dir path/to/output
```

### Example

Suppose you have the following directory structure:

```
project/
├── generate_markdown.py
├── src/
│   ├── module1.py
│   └── module2.py
└── docs/
```

You can generate Markdown files for the Python files in the `src/` directory and save them in the `docs/` directory with the following command:

```bash
python generate_markdown.py --input_dir src --output_dir docs
```

This will create Markdown files in the `docs/` directory, each containing an `mkdocstrings` directive to include the documentation for the corresponding Python module.

### Output

The generated Markdown files will have the same base name as the Python files but with a `.md` extension. Each file will contain a header with the file name and an `mkdocstrings` directive to include the documentation for the corresponding Python module.

For example, if you have a `module1.py` file in the `src/` directory, the script will generate a `module1.md` file in the `docs/` directory with the following content:

```markdown
# module1.py

::: src.module1
```

This allows you to easily integrate the generated documentation into your documentation site using MkDocs and mkdocstrings.

## Note

Ensure that the `mkdocstrings` plugin is configured in your MkDocs `mkdocs.yml` file to correctly render the documentation from the generated Markdown files.

Here is an example `mkdocs.yml` configuration:

```yaml
site_name: My Project Documentation
nav:
  - Home: index.md
  - API:
      - Module 1: docs/module1.md
      - Module 2: docs/module2.md
plugins:
  - search
  - mkdocstrings:
      handlers:
        python:
          rendering:
            show_source: true
```

This configuration will include the generated documentation in your MkDocs site.
