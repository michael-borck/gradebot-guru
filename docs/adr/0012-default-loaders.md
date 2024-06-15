# ADR 0012: Implement Default Loaders for Submissions

## Status
Accepted

## Context
Student submissions can come in various formats, including text files, Markdown, PDFs, DOCX, and code files (e.g., Python, JavaScript, CSS, HTML). The current implementation assumes that all submissions are plain text, which is not realistic or scalable. To improve usability and flexibility, we need to handle different file formats robustly.

## Decision
We will implement default loaders for common submission formats, including:

1. **Text Loader:** Handles plain text files.
2. **Markdown Loader:** Parses Markdown files.
3. **PDF Loader:** Extracts text from PDF files.
4. **DOCX Loader:** Extracts text from DOCX files.
5. **Code Loaders:** Handles various programming languages (Python, JavaScript, CSS, HTML, etc.).

### Implementation

#### submission_loader.py

```python
import os
from typing import Any, Dict

def load_text(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def load_markdown(file_path: str) -> str:
    return load_text(file_path)

def load_pdf(file_path: str) -> str:
    try:
        from PyPDF2 import PdfFileReader
        with open(file_path, 'rb') as file:
            reader = PdfFileReader(file)
            return ' '.join(page.extract_text() for page in reader.pages)
    except ImportError:
        raise ImportError("PyPDF2 is required to load PDF files")

def load_docx(file_path: str) -> str:
    try:
        import docx
        doc = docx.Document(file_path)
        return ' '.join(paragraph.text for paragraph in doc.paragraphs)
    except ImportError:
        raise ImportError("python-docx is required to load DOCX files")

def load_code(file_path: str) -> str:
    return load_text(file_path)

def load_submission(file_path: str) -> str:
    _, file_extension = os.path.splitext(file_path)
    loaders = {
        '.txt': load_text,
        '.md': load_markdown,
        '.pdf': load_pdf,
        '.docx': load_docx,
        '.py': load_code,
        '.js': load_code,
        '.css': load_code,
        '.html': load_code,
    }
    loader = loaders.get(file_extension.lower())
    if loader:
        return loader(file_path)
    else:
        raise ValueError(f"Unsupported file format: {file_extension}")

# Example usage:
# submission_content = load_submission('path_to_file')
```

### Unit Tests for `submission_loader.py`

#### test_submission_loader.py

```python
import pytest
from submission_loader import load_text, load_markdown, load_pdf, load_docx, load_code, load_submission

def test_load_text(tmp_path):
    text_file = tmp_path / "test.txt"
    text_file.write_text("This is a test text file.")
    assert load_text(str(text_file)) == "This is a test text file."

def test_load_markdown(tmp_path):
    md_file = tmp_path / "test.md"
    md_file.write_text("# Test\nThis is a test markdown file.")
    assert load_markdown(str(md_file)) == "# Test\nThis is a test markdown file."

def test_load_pdf(tmp_path):
    from PyPDF2 import PdfFileWriter
    pdf_file = tmp_path / "test.pdf"
    writer = PdfFileWriter()
    writer.add_blank_page(width=72, height=72)
    with open(pdf_file, 'wb') as f:
        writer.write(f)
    assert load_pdf(str(pdf_file)) == ""

def test_load_docx(tmp_path):
    import docx
    docx_file = tmp_path / "test.docx"
    doc = docx.Document()
    doc.add_paragraph("This is a test DOCX file.")
    doc.save(docx_file)
    assert load_docx(str(docx_file)) == "This is a test DOCX file."

def test_load_code(tmp_path):
    code_file = tmp_path / "test.py"
    code_file.write_text("print('Hello, world!')")
    assert load_code(str(code_file)) == "print('Hello, world!')"

def test_load_submission(tmp_path):
    text_file = tmp_path / "test.txt"
    text_file.write_text("This is a test text file.")
    assert load_submission(str(text_file)) == "This is a test text file."

    md_file = tmp_path / "test.md"
    md_file.write_text("# Test\nThis is a test markdown file.")
    assert load_submission(str(md_file)) == "# Test\nThis is a test markdown file."

    # Add tests for PDF, DOCX, and code files similarly

if __name__ == "___MAIN__":
    pytest.main()
```

## Consequences
### Positive
- Improved usability and flexibility by supporting multiple submission formats.
- Reduced burden on users to preprocess submissions into a compatible format.
- Easier future expansion to support additional formats.

### Negative
- Increased complexity in the `submission_loader.py` implementation.
- Additional dependencies (e.g., PyPDF2, python-docx) required for handling certain formats.

## Next Steps
- Implement the default loaders as described above.
- Add unit tests to ensure each loader functions correctly.
- Update the documentation to reflect the new capabilities and any additional dependencies.
