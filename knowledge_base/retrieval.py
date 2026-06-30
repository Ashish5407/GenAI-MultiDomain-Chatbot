
from langchain_community.vectorstores import FAISS
from medical_chatbot.embeddings import get_embedding_model
from utils.config import VECTOR_DB_DIR

DB_PATH = VECTOR_DB_DIR / "knowledge_db"
embeddings = get_embedding_model()


def retrieve_knowledge(query, k=3):

    if not DB_PATH.exists():
        return []
    
    db = FAISS.load_local(str(DB_PATH), embeddings, allow_dangerous_deserialization=True)

    docs = db.similarity_search(query, k=k)

    return docs
