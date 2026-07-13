
from utils.memory import memory
from utils.logger import logger
from router.query_classifier import classify_query

# Task 1
from sentiment.sentiment import detect_sentiment
from sentiment.responses import sentiment_response

# Task 2
from medical_chatbot.chatbot import medical_chatbot

# Task 3
from knowledge_base.chatbot import knowledge_chatbot

# Task 4
from research_expert.paper_search import search_papers
from research_expert.summarizer import summarize_paper
from research_expert.explainer import explain_paper

# Task 5
from multimodal.multimodal_chat import process_uploaded_file

# Task 6
from multilingual.multilingual_chat import multilingual_response

# General Chat
from utils.gemini import general_chat


def route_query(user_input, uploaded_file=None):
    user_input = str(user_input).strip()

    if not user_input:
        return "Please enter a message."

    module = classify_query(user_input, uploaded_file)
    
    memory.current_module = module
    memory.last_query = user_input

    try:

        if module == "multimodal":

            if uploaded_file is None:
                response = "Please upload a file first."

            else:
                response = process_uploaded_file(
                    uploaded_file,
                    user_input
                )

        elif module == "medical":
            response = medical_chatbot(user_input)

        elif module == "knowledge":
            response = knowledge_chatbot(user_input)

        elif module == "research":
            papers = search_papers(user_input)

            if not papers:
                response = "No research papers found."

            else:
                paper = papers[0]
                memory.last_paper = paper

                if "explain" in user_input.lower():
                    response = explain_paper(paper)

                else:
                    response = summarize_paper(paper)

        elif module == "sentiment":
            sentiment = detect_sentiment(user_input)
            response = sentiment_response(sentiment)

        elif module == "multilingual":
            english_response = general_chat(user_input)
            response = multilingual_response(user_input, english_response)

        else:
            response = general_chat(user_input)

    except Exception as e:
        response = f"Error: {str(e)}"

    memory.last_response = response

    return response