
from medical_chatbot.retrieval import retrieve_answer
from medical_chatbot.medical_ner import extract_entities
from knowledge_base.retrieval import retrieve_knowledge
from utils.gemini import model
from utils.logger import logger


def medical_chatbot(query):
    medical_results = retrieve_answer(query)
    knowledge_results = retrieve_knowledge(query)
    
    medical_context = "\n\n".join(
        [
            f"Question: {doc['question']}\nAnswer: {doc['answer']}"
            for doc in medical_results
        ]
    )
    
    knowledge_context = ""

    if knowledge_results:
        knowledge_context = "\n\n".join(
            [
                doc.page_content
                for doc in knowledge_results
            ]
        )
    
    context = f"""
    Medical Database:{medical_context}
    Additional Knowledge:{knowledge_context} """
    
    entities = extract_entities(query)

    prompt = f""" You are a helpful medical assistant.
                Use the following context to answer the user's question.

    Context: {context}
    Extracted Medical Entities: {entities}
    User Question: {query}

    Provide a clear and concise answer.
    If the answer is not available in the context, say you don't know. """

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        logger.error(f"Medical chatbot failed to generate a response: {e}")
        return f"Error: {str(e)}"


if __name__ == "__main__":
    while True:
        query = input("\nAsk a medical question: ")

        if query.lower() == "exit":
            break

        print("\nAnswer:")
        print(medical_chatbot(query))