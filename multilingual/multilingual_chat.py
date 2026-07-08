
from multilingual.language_detector import detect_language
from utils.gemini import model


LANGUAGE_NAMES = {
    "en": "English",
    "hi": "Hindi",
    "ta": "Tamil",
    "te": "Telugu",
    "kn": "Kannada",
    "ml": "Malayalam",
    "fr": "French",
    "de": "German",
    "es": "Spanish",
    "it": "Italian",
    "ja": "Japanese",
    "ko": "Korean",
    "zh-cn": "Chinese",
    "zh-tw": "Chinese"
}


def multilingual_response(user_message, chatbot_response):
    language = detect_language(user_message)

    if language == "en":
        return chatbot_response

    language_name = LANGUAGE_NAMES.get(language, "English")

    prompt = f""" Translate the following response into {language_name}.
Do not change the meaning. Keep formatting unchanged.
Response: {chatbot_response} """

    try:
        response = model.generate_content(prompt)
        return response.text
    
    except Exception as e:
        return f"Error: {str(e)}"