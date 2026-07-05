
from multimodal.file_handler import save_uploaded_file
from multimodal.document_reader import extract_document_text
from multimodal.spreadsheet_reader import extract_spreadsheet
from multimodal.image_analyzer import analyze_image
from multimodal.reasoning import reason_over_content


def process_uploaded_file(uploaded_file, user_question):
    """ Automatically processes any uploaded file and returns the chatbot response. """

    file_path, file_type = save_uploaded_file(uploaded_file)

    if file_type == "image":
        return analyze_image(file_path, user_question)

    elif file_type == "document":
        content = extract_document_text(file_path)
        return reason_over_content(content, user_question)

    elif file_type == "spreadsheet":
        content = extract_spreadsheet(file_path)
        return reason_over_content(content, user_question)

    return "Unsupported file format."