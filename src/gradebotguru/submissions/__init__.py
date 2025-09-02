"""Submissions package for text extraction utilities."""

from .extract import (
    extract_text_from_docx,
    extract_text_from_pdf,
    process_files_in_folder,
)

__all__ = ["extract_text_from_pdf", "extract_text_from_docx", "process_files_in_folder"]
