
from utils.gemini import model


def extract_entities(text):
    prompt = f""" Extract medical entities from the following text.

Identify:
    - Symptoms
    - Diseases
    - Treatments/Medications

Return only a Python dictionary in this format:
        {{
        "symptoms": [],
        "diseases": [],
        "treatments": []
        }}

Text: {text} """

    response = model.generate_content(prompt)

    return response.text


if __name__ == "__main__":
    text = input("Enter text: ")

    entities = extract_entities(text)

    print(entities)