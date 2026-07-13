
import os
import faiss
import pickle
from sentence_transformers import SentenceTransformer
from medical_chatbot.medquad_loader import load_medquad
from utils.config import MEDICAL_DB_DIR

_model = None


def get_sentence_model():
    global _model
    if _model is None:
        _model = SentenceTransformer("all-MiniLM-L6-v2")
    return _model


def get_embedding_model():
    from langchain_huggingface import HuggingFaceEmbeddings
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )


def create_vector_db():
    documents = load_medquad()

    model = get_sentence_model()
    questions = [doc["question"] for doc in documents]
    embeddings = model.encode(questions, show_progress_bar=True)

    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    os.makedirs(MEDICAL_DB_DIR, exist_ok=True)

    faiss.write_index(index, str(MEDICAL_DB_DIR / "medical_index.faiss"))

    with open(MEDICAL_DB_DIR / "documents.pkl", "wb") as f:
        pickle.dump(documents, f)

    print("Medical vector database created successfully!")


if __name__ == "__main__":
    create_vector_db()
