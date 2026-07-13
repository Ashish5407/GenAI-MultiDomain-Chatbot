
import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer
from utils.config import MEDICAL_DB_DIR
from utils.logger import logger

_model = None
_index = None
_documents = None


def _load_resources():
    global _model, _index, _documents

    if _model is not None:
        return True

    index_path = MEDICAL_DB_DIR / "medical_index.faiss"
    docs_path = MEDICAL_DB_DIR / "documents.pkl"

    if not index_path.exists() or not docs_path.exists():
        logger.warning("Medical FAISS index not found. Run medical_chatbot/embeddings.py first.")
        return False

    try:
        _model = SentenceTransformer("all-MiniLM-L6-v2")
        _index = faiss.read_index(str(index_path))

        with open(docs_path, "rb") as f:
            _documents = pickle.load(f)

        logger.info("Medical FAISS index loaded successfully.")
        return True

    except Exception as e:
        logger.error(f"Failed to load medical index: {e}")
        return False


def retrieve_answer(query, k=1):

    if not _load_resources():
        return []

    try:
        query_embedding = _model.encode([query])
        distances, indices = _index.search(query_embedding, k)

        results = []
        for idx in indices[0]:
            if idx < len(_documents):
                results.append(_documents[idx])

        return results

    except Exception as e:
        logger.error(f"Medical retrieval error: {e}")
        return []
