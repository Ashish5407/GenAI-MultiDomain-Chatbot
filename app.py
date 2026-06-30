
import os
import streamlit as st
from sentiment.sentiment import detect_sentiment
from sentiment.responses import sentiment_response
from medical_chatbot.chatbot import medical_chatbot
from knowledge_base.updater import update_knowledge_base
from utils.config import UPLOADS_DIR

st.set_page_config(
    page_title="GenAI Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 GenAI Assistant")

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "Sentiment",
    "Medical QA",
    "Knowledge Base",
    "Research Expert",
    "Multimodal",
    "Multilingual"
])


# TASK 1 - SENTIMENT

with tab1:
    st.header("Sentiment Analysis")

    text = st.text_area("Enter a message", key="sentiment_text")

    if st.button("Analyze Sentiment"):
        sentiment = detect_sentiment(text)
        st.success(f"Detected Sentiment: {sentiment}")
        st.write(sentiment_response(sentiment))


# TASK 2 - MEDICAL QA

with tab2:
    st.header("Medical Question Answering")

    query = st.text_input("Ask a medical question", key="medical_query")

    if st.button("Get Medical Answer"):
        answer = medical_chatbot(query)
        st.write(answer)


# TASK 3 - KNOWLEDGE BASE


with tab3:
    st.header("Knowledge Base Updater")

    uploaded_file = st.file_uploader(
        "Upload PDF / TXT / Image",
        type=["pdf", "txt", "png", "jpg", "jpeg"] )

    if uploaded_file:
        UPLOADS_DIR.mkdir(parents=True, exist_ok=True)
        
        file_path = UPLOADS_DIR / uploaded_file.name
        
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success(f"{uploaded_file.name} uploaded successfully.")

        if st.button("Update Knowledge Base"):
            update_knowledge_base(file_path)
            st.success("Knowledge Base Updated Successfully!")

    st.divider()
    st.subheader("Add Website / YouTube Knowledge")

    source_url = st.text_input("Enter Website or YouTube URL")
    
    if st.button("Add URL Source"):
        if source_url:
            update_knowledge_base(source_url)
            st.success("Knowledge Base Updated Successfully!")
        else: 
            st.warning("Please enter a valid URL")


# TASK 4

with tab4:

    st.info("Research Expert - Coming Soon")


# TASK 5

with tab5:

    st.info("Multimodal Assistant - Coming Soon")


# TASK 6

with tab6:

    st.info("Multilingual Assistant - Coming Soon")
