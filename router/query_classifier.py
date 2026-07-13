
import re
from multilingual.language_detector import detect_language
from utils.logger import logger

MEDICAL_KEYWORDS = {
    "fever", "headache", "pain", "doctor", "medicine", "disease", "symptom",
    "hospital", "medical", "health", "covid", "diabetes", "infection",
    "blood", "heart", "cancer", "treatment", "tablet", "drug", "vaccine",
    "virus", "bacteria", "injury", "fracture", "nausea", "vomiting", "cough",
    "cold", "asthma", "kidney", "liver", "brain", "pregnancy", "surgery"
}

RESEARCH_KEYWORDS = {
    "research", "paper", "journal", "study", "citation", "author",
    "abstract", "publication", "doi", "arxiv", "summarize",
    "summary", "explain paper", "research paper"
}

KNOWLEDGE_KEYWORDS = {
    "knowledge", "knowledge base", "update", "learn",
    "remember", "store", "save", "upload"
}

SENTIMENT_KEYWORDS = {
    "happy", "sad", "angry", "upset", "emotion", "feeling",
    "depressed", "excited", "lonely", "stress", "anxiety"
}

WORD_PATTERN = re.compile(r"\b\w+\b")


def contains_keyword(text, keywords):
    words = set(WORD_PATTERN.findall(text))

    for keyword in keywords:
        keyword_words = keyword.split()

        if len(keyword_words) == 1:
            if keyword in words:
                return True
        else:
            if keyword in text:
                return True

    return False


def classify_query(user_input, uploaded_file=None):
    text = str(user_input).strip().lower()

    if not text:
        logger.warning("Received empty user input.")
        return "general"

    if uploaded_file is not None:
        logger.info("Intent detected: multimodal")
        return "multimodal"

    if contains_keyword(text, KNOWLEDGE_KEYWORDS):
        logger.info("Intent detected: knowledge")
        return "knowledge"

    if contains_keyword(text, RESEARCH_KEYWORDS):
        logger.info("Intent detected: research")
        return "research"

    if contains_keyword(text, MEDICAL_KEYWORDS):
        logger.info("Intent detected: medical")
        return "medical"

    if contains_keyword(text, SENTIMENT_KEYWORDS):
        logger.info("Intent detected: sentiment")
        return "sentiment"

    language = detect_language(text)

    if language != "en":
        logger.info("Intent detected: multilingual")
        return "multilingual"

    logger.info("Intent detected: general")
    return "general"