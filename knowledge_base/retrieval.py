
from langchain_community.vectorstores import FAISS
from utils.config import VECTOR_DB_DIR
from utils.logger import logger

DB_PATH = VECTOR_DB_DIR / "knowledge_db"

_embeddings = None


def _get_embeddings():
    global _embeddings
    if _embeddings is None:
        from medical_chatbot.embeddings import get_embedding_model
        _embeddings = get_embedding_model()
    return _embeddings


def retrieve_knowledge(query, k=3):

    if not (DB_PATH / "index.faiss").exists():
        return []

    try:
        db = FAISS.load_local(
            str(DB_PATH),
            _get_embeddings(),
            allow_dangerous_deserialization=True
        )
        docs = db.similarity_search(query, k=k)
        return docs

    except Exception as e:
        logger.error(f"Knowledge base retrieval error: {e}")
        return []
