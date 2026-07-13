
from PIL import Image
from utils.gemini import model


def analyze_image(image_path, prompt=None):
    """ Analyze an image or answer a question about it. """

    image = Image.open(image_path)

    if prompt is None:
        prompt = """ Analyze this image in detail.
        Mention:
        - Main objects
        - Text (if any)
        - Charts or diagrams
        - Tables
        - Important observations """

    try:
        response = model.generate_content([prompt, image])
        return response.text

    except Exception as e:
        return f"Error: {str(e)}"