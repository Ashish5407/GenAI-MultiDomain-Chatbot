
from utils.gemini import model
from knowledge_base.retrieval import retrieve_knowledge


def knowledge_chatbot(query):
    """ Answers questions using the Knowledge Base. """

    documents = retrieve_knowledge(query)

    if not documents:
        return "I couldn't find any relevant information in the knowledge base."

    context = "\n\n".join(
        doc.page_content
        for doc in documents
    )

    prompt = f"""
You are an intelligent knowledge base assistant.
Use ONLY the information provided below.
If the answer is not present in the context,
say: "I couldn't find that information in the knowledge base."

Context: {context}
Question: {query}

Answer: """

    try:
        response = model.generate_content(prompt)
        return response.text
    
    except Exception as e:
        return f"Error: {str(e)}"