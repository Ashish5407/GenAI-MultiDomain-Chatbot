
import fitz
from docx import Document


def read_pdf(file_path):
    text = ""
    pdf = fitz.open(file_path)
    for page in pdf:
        text += page.get_text()
    pdf.close()
    return text


def read_docx(file_path):
    document = Document(file_path)
    text = "\n".join(
        paragraph.text
        for paragraph in document.paragraphs
    )
    return text


def read_txt(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def extract_document_text(file_path):
    extension = str(file_path).split(".")[-1].lower()

    if extension == "pdf":
        return read_pdf(file_path)

    elif extension == "docx":
        return read_docx(file_path)

    elif extension == "txt":
        return read_txt(file_path)

    else:
        raise ValueError("Unsupported document format.")