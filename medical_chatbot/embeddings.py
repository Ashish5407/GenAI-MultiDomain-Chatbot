
import os
import faiss
import pickle
from sentence_transformers import SentenceTransformer
from medical_chatbot.medquad_loader import load_medquad
from utils.config import MEDICAL_DB_DIR
from langchain_huggingface import HuggingFaceEmbeddings     

model = SentenceTransformer("all-MiniLM-L6-v2")

def create_vector_db():
    documents = load_medquad()

    questions = [doc["question"] for doc in documents]
    embeddings = model.encode(questions)

    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    os.makedirs(MEDICAL_DB_DIR, exist_ok=True)

    faiss.write_index(index, f"{MEDICAL_DB_DIR}/medical_index.faiss")

    with open(f"{MEDICAL_DB_DIR}/documents.pkl", "wb") as f:
        pickle.dump(documents, f)

    print("Medical vector database created successfully!")


def get_embedding_model():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )