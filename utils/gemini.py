
import os
import google.generativeai as genai
from dotenv import load_dotenv
from utils.logger import logger

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    logger.warning("GOOGLE_API_KEY is not set. Gemini calls will fail.")

genai.configure(api_key=GOOGLE_API_KEY)

generation_config = {
    "temperature": 0.3,
    "top_p": 0.9,
    "top_k": 40,
    "max_output_tokens": 2048,
}

model = genai.GenerativeModel("gemini-2.5-flash", generation_config=generation_config,)

def general_chat(user_input):
    try:
        response = model.generate_content(user_input)
        return response.text

    except Exception as e:
        logger.error(f"Gemini call failed: {e}")
        return f"Error: {str(e)}"