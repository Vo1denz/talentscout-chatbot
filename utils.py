import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel(model_name="gemini-2.5-flash")

def ask_gemini(prompt):
    try:
        response = model.generate_content(prompt)
        return response
    except Exception as e:
        return type('Response', (), {'text': f"❌ Gemini Error: {e}"})()
