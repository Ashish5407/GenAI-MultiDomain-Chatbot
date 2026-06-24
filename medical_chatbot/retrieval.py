
import faiss
import pickle
from sentence_transformers import SentenceTransformer
from utils.config import MEDICAL_DB_DIR

model = SentenceTransformer("all-MiniLM-L6-v2")

index = faiss.read_index(f"{MEDICAL_DB_DIR}/medical_index.faiss")

with open(f"{MEDICAL_DB_DIR}/documents.pkl", "rb") as f:
    documents = pickle.load(f)

def retrieve_answer(query, k=1):
    query_embedding = model.encode([query])

    distances, indices = index.search(query_embedding, k)

    results = []
    for idx in indices[0]:
        results.append(documents[idx])

    return results  
