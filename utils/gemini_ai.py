import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def explain_encryption(code_snippet):
    prompt = f"Explain the following encryption code in simple terms:\n{code_snippet}"
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    return response.text

def translate_text(text, target_language):
    prompt = f"Translate this into {target_language}:\n\n{text}"
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    return response.text
