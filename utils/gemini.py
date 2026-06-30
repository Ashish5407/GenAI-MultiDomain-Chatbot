
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

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
        return f"Error: {str(e)}"