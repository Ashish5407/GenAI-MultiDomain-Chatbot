
from utils.gemini import model

MAX_CONTENT_LENGTH = 15000


def reason_over_content(content, question):
    """ Performs reasoning over extracted text from documents, spreadsheets, or other supported file types. """

    if not content or not content.strip():
        return "No content found to analyze."

    if len(content) > MAX_CONTENT_LENGTH:
        content = content[:MAX_CONTENT_LENGTH]

    prompt = f""" You are an intelligent AI assistant.
Answer the user's question ONLY using the provided content.
If the answer is not present in the content,
say: "I couldn't find that information in the uploaded file."
Content: {content}
User Question: {question}
Answer: """

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"Error: {str(e)}"