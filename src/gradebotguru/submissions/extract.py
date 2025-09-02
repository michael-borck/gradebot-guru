import os

import docx
import PyPDF2


def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extract text from a single PDF file.

    Args:
        pdf_path (str): Path to the PDF file.

    Returns:
        str: Extracted text from the PDF.
    """
    text = ""
    with open(pdf_path, "rb") as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text


def extract_text_from_docx(docx_path: str) -> str:
    """
    Extract text from a single DOCX file.

    Args:
        docx_path (str): Path to the DOCX file.

    Returns:
        str: Extracted text from the DOCX file.
    """
    doc = docx.Document(docx_path)
    text = []
    for para in doc.paragraphs:
        text.append(para.text)
    return "\n".join(text)


def process_files_in_folder(folder_path: str) -> None:
    """
    Process all PDF and DOCX files in a folder, extracting the text and saving it as a .txt file.

    Args:
        folder_path (str): Path to the folder containing PDF and DOCX files.
    """
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if filename.endswith(".pdf"):
            print(f"Processing PDF file: {file_path}")

            # Extract text from the PDF
            extracted_text = extract_text_from_pdf(file_path)

            # Save the extracted text to a .txt file
            txt_filename = os.path.splitext(filename)[0] + ".txt"
            txt_path = os.path.join(folder_path, txt_filename)

            with open(txt_path, "w", encoding="utf-8") as txt_file:
                txt_file.write(extracted_text)
                print(f"Saved text to: {txt_path}")

        elif filename.endswith(".docx"):
            print(f"Processing DOCX file: {file_path}")

            # Extract text from the DOCX
            extracted_text = extract_text_from_docx(file_path)

            # Save the extracted text to a .txt file
            txt_filename = os.path.splitext(filename)[0] + ".txt"
            txt_path = os.path.join(folder_path, txt_filename)

            with open(txt_path, "w", encoding="utf-8") as txt_file:
                txt_file.write(extracted_text)
                print(f"Saved text to: {txt_path}")


if __name__ == "__main__":
    # Set the folder path containing the PDF and DOCX files
    folder_path = input("Enter the folder path containing PDF and DOCX files: ")

    if os.path.isdir(folder_path):
        process_files_in_folder(folder_path)
        print("Processing completed.")
    else:
        print(f"The folder path '{folder_path}' does not exist.")
