
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


# Project Directories

DATA_DIR = BASE_DIR / "data"
VECTOR_DB_DIR = BASE_DIR / "vector_db"

MEDQUAD_DIR = DATA_DIR / "MedQuAD"
ARXIV_DIR = DATA_DIR / "arxiv"

UPLOADS_DIR = DATA_DIR / "uploads"
IMAGE_UPLOADS_DIR = UPLOADS_DIR / "images"


# Vector Databases

MEDICAL_DB_DIR = VECTOR_DB_DIR / "medical_db"
KNOWLEDGE_DB_DIR = VECTOR_DB_DIR / "knowledge_db"
RESEARCH_DB_DIR = VECTOR_DB_DIR / "research_db"


# Supported File Types

SUPPORTED_IMAGES = IMAGE_EXTENSIONS = {
    "jpg",
    "jpeg",
    "png",
    "webp"
}

SUPPORTED_DOCUMENTS = DOCUMENT_EXTENSIONS = {
    "pdf",
    "docx",
    "txt"
}

SUPPORTED_SPREADSHEETS = SPREADSHEET_EXTENSIONS = {
    "csv",
    "xlsx"
}

SUPPORTED_EXTENSIONS = (
    SUPPORTED_IMAGES
    | SUPPORTED_DOCUMENTS
    | SUPPORTED_SPREADSHEETS
)


# Creates files if not exist

for folder in [
    DATA_DIR,
    VECTOR_DB_DIR,
    UPLOADS_DIR,
    IMAGE_UPLOADS_DIR,
    MEDICAL_DB_DIR,
    KNOWLEDGE_DB_DIR,
    RESEARCH_DB_DIR,
]:
    folder.mkdir(parents=True, exist_ok=True)