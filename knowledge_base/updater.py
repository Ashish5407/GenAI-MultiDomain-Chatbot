
import shutil
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from medical_chatbot.embeddings import get_embedding_model
from knowledge_base.source_loader import load_source
from utils.config import UPLOADS_DIR, KNOWLEDGE_DB_DIR
from utils.logger import logger


def update_knowledge_base(source):

    UPLOADS_DIR.mkdir(parents=True, exist_ok=True)
    KNOWLEDGE_DB_DIR.mkdir(parents=True, exist_ok=True)

    if isinstance(source, str) and (
        source.startswith("http://")
        or source.startswith("https://")
    ):

        docs = load_source(source)
        source_name = source

    else:
        source_path = source
        destination = UPLOADS_DIR / source_path.name

        if source_path != destination and not destination.exists():
            shutil.copy(source_path, destination)

        docs = load_source(str(destination))
        source_name = destination.name

    if not docs:
        logger.warning(f"No documents found for source: {source_name}")
        return

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)

    chunks = splitter.split_documents(docs)

    embeddings = get_embedding_model()

    if (KNOWLEDGE_DB_DIR / "index.faiss").exists():
        db = FAISS.load_local(str(KNOWLEDGE_DB_DIR), embeddings, allow_dangerous_deserialization=True)
        db.add_documents(chunks)

    else:
        db = FAISS.from_documents(chunks, embeddings)

    db.save_local(str(KNOWLEDGE_DB_DIR))

    logger.info(f"Knowledge base updated from {source_name}")