
from langchain_community.document_loaders import (
    WebBaseLoader,
    PyPDFLoader,
    TextLoader,
    UnstructuredImageLoader,
    YoutubeLoader
)
import os


def load_source(source):

    # Website
    if source.startswith("http") and "github.com" not in source and "youtube.com" not in source:
        return WebBaseLoader(source).load()

    # YouTube
    elif "youtube.com" in source:
        return YoutubeLoader.from_youtube_url(source, add_video_info=True).load()

    # PDF
    elif source.endswith(".pdf"):
        return PyPDFLoader(source).load()

    # TXT
    elif source.endswith(".txt"):
        return TextLoader(source).load()

    # Image
    elif source.endswith((".png", ".jpg", ".jpeg")):
        return UnstructuredImageLoader(source).load()

    return []

