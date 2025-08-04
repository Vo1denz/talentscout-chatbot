import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel(model_name="gemini-2.5-flash")

try:
    response = model.generate_content("Say hello!")
    print("✅ Gemini responded:")
    print(response.text)  # <-- This line prints the actual reply
except Exception as e:
    print("❌ Error occurred:")
    print(e)
