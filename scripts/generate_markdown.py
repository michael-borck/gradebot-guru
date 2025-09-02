import argparse
import os


def generate_markdown_from_python(input_dir: str, output_dir: str) -> None:
    """
    Generate Markdown files with mkdocstrings directives for all Python files in the specified input directory.

    Args:
        input_dir (str): The directory containing Python files.
        output_dir (str): The directory to save the generated Markdown files.
    """
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, input_dir)
                module_path = relative_path.replace(os.sep, ".").rsplit(".", 1)[0]

                # Add the folder structure to the module path
                module_path = f"{input_dir.replace(os.sep, '.')}{module_path}"

                markdown_content = f"# {file}\n\n::: {module_path}\n"
                output_file_path = os.path.join(
                    output_dir, f"{os.path.splitext(file)[0]}.md"
                )

                with open(output_file_path, "w") as md_file:
                    md_file.write(markdown_content)
                print(f"Generated: {output_file_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate Markdown files for Python files with mkdocstrings directives."
    )
    parser.add_argument(
        "--input_dir",
        type=str,
        default=".",
        help="Input directory containing Python files (default: current directory)",
    )
    parser.add_argument(
        "--output_dir",
        type=str,
        default=".",
        help="Output directory for generated Markdown files (default: current directory)",
    )

    args = parser.parse_args()

    generate_markdown_from_python(args.input_dir, args.output_dir)
