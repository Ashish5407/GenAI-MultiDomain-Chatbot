
import streamlit as st
from router.intent_router import route_query
from knowledge_base.updater import update_knowledge_base
from utils.memory import memory
from utils.config import UPLOADS_DIR
from utils.logger import logger

# Page Configuration

st.set_page_config(
    page_title="GenAI Multi-Domain Chatbot",
    page_icon="🤖",
    layout="wide"
)

# Session State (UI only, chat history lives in utils/memory)

if "current_file" not in st.session_state:
    st.session_state.current_file = None

if "uploaded_files_log" not in st.session_state:
    st.session_state.uploaded_files_log = []

# Helper Functions

def display_chat():
    for entry in memory.get_history():
        with st.chat_message(entry["role"]):
            st.markdown(entry["message"])


def save_to_uploads(uploaded_file):
    UPLOADS_DIR.mkdir(parents=True, exist_ok=True)
    file_path = UPLOADS_DIR / uploaded_file.name

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    logger.info(f"Uploaded file saved: {uploaded_file.name}")

    return file_path


def log_uploaded_file(uploaded_file):
    if uploaded_file.name not in st.session_state.uploaded_files_log:
        st.session_state.uploaded_files_log.append(uploaded_file.name)

# Sidebar

with st.sidebar:

    st.title("🤖 GenAI Chatbot")

    st.markdown("---")

    st.subheader("📂 Upload File")

    uploaded_file = st.file_uploader(
        "Choose a file",
        type=["pdf", "docx", "txt", "csv", "xlsx", "png", "jpg", "jpeg"]
    )

    if uploaded_file is not None:
        st.session_state.current_file = uploaded_file
        log_uploaded_file(uploaded_file)

    st.markdown("---")

    st.subheader("🌐 Website URL")

    website_url = st.text_input("Website URL", placeholder="https://...")

    st.markdown("---")

    st.subheader("🎥 YouTube URL")

    youtube_url = st.text_input("YouTube URL", placeholder="https://youtube.com/...")

    st.markdown("---")

    if st.button("📥 Update Knowledge Base", use_container_width=True):

        added_source = False

        if st.session_state.current_file is not None:
            try:
                file_path = save_to_uploads(st.session_state.current_file)
                update_knowledge_base(file_path)
                added_source = True
            except Exception as e:
                logger.error(f"Knowledge base file update failed: {e}")
                st.error(f"File: {e}")

        try:
            if website_url.strip():
                update_knowledge_base(website_url)
                added_source = True
        except Exception as e:
            logger.error(f"Website indexing failed: {e}")
            st.error(f"Website: {e}")
        
        try:
            if youtube_url.strip():
                update_knowledge_base(youtube_url)
                added_source = True
        except Exception as e:
            logger.error(f"YouTube indexing failed: {e}")
            st.error(f"YouTube: {e}")

        if added_source:
            logger.info("Knowledge base updated successfully.")
            st.success("Knowledge base updated.")
        else:
            st.warning("Upload a file or enter a URL first.")

    st.markdown("---")

    if st.button("🗑 Clear Chat", use_container_width=True):
        memory.clear_history()
        logger.info("Chat history cleared.")
        memory.reset_uploaded_file()
        st.session_state.current_file = None
        st.rerun()

    st.markdown("---")

    with st.expander("🌍 Supported Languages"):
        st.write(
            "English, Hindi, Tamil, Telugu, Kannada, Malayalam, "
            "French, German, Spanish, Italian, Japanese, Korean, Chinese"
        )
        st.caption("Language is detected automatically from your message.")

    st.markdown("---")

    st.subheader("Uploaded Files")

    if len(st.session_state.uploaded_files_log) == 0:
        st.info("No files uploaded yet.")
    else:
        for name in st.session_state.uploaded_files_log:
            st.caption(f"📄 {name}")


# Main Page

st.title("🤖 GenAI Multi-Domain Chatbot")

st.caption(
    "Medical Q&A • Research Papers • Knowledge Base • "
    "Multimodal Files • Sentiment • Multilingual"
)

st.markdown("---")

if memory.get_history():
    display_chat()

# Chat Input

prompt = st.chat_input("Ask me anything...")

if prompt:

    memory.add_message("user", prompt)
    logger.info("User message received.")

    with st.chat_message("user"):
        st.markdown(prompt)

    chat_file = st.session_state.current_file

    if chat_file is not None:
        if hasattr(chat_file, "seek"):
            chat_file.seek(0)

    with st.chat_message("assistant"):


        with st.spinner("Generating response..."):
            try:
                response = route_query(prompt, chat_file)
            except Exception as e:
                logger.exception("Error while routing user query.")
                response = f"Error: {e}"
            st.markdown(response)

    memory.add_message("assistant", response)
    logger.info("Assistant response generated.")