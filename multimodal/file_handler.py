
import os
import shutil
from uuid import uuid4
from utils.memory import memory

from utils.config import (
    UPLOADS_DIR,
    SUPPORTED_EXTENSIONS,
    IMAGE_EXTENSIONS,
    DOCUMENT_EXTENSIONS,
    SPREADSHEET_EXTENSIONS
)

UPLOADS_DIR.mkdir(parents=True, exist_ok=True)


def save_uploaded_file(uploaded_file):
    """ Saves the uploaded file and returns: file_path, file_type """

    extension = uploaded_file.name.split(".")[-1].lower()

    filename = f"{uuid4()}.{extension}"

    file_path = UPLOADS_DIR / filename

    with open(file_path, "wb") as f:
        shutil.copyfileobj(uploaded_file, f)

    if extension in IMAGE_EXTENSIONS:
        file_type = "image"

    elif extension in DOCUMENT_EXTENSIONS:
        file_type = "document"

    elif extension in SPREADSHEET_EXTENSIONS:
        file_type = "spreadsheet"

    else:
        file_type = "unknown"

    memory.set_uploaded_file(file_path, file_type)

    if file_type == "image":
        memory.set_last_image(file_path)
    
    return file_path, file_type