
from langdetect import detect, DetectorFactory

DetectorFactory.seed = 0


def detect_language(text):
    """ Detects the language of the user's message. Returns language code like: en, hi, ta, fr, de... """

    try:
        return detect(text)

    except Exception:
        return "en"