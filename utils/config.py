
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
VECTOR_DB_DIR = BASE_DIR / "vector_db"

MEDQUAD_DIR = DATA_DIR / "MedQuAD"
ARXIV_DIR = DATA_DIR / "arxiv"
UPLOADS_DIR = DATA_DIR / "uploads"

MEDICAL_DB_DIR = "vector_db/medical_db"
KNOWLEDGE_DB_DIR = VECTOR_DB_DIR / "knowledge_db"

