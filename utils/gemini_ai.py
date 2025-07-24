import google.generativeai as genai
import os

# Load Gemini API key from Streamlit secrets
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

# Generic Gemini prompt wrapper
def ask_gemini(prompt, model="models/gemini-pro", temperature=0.7):
    chat = genai.GenerativeModel(model).start_chat()
    response = chat.send_message(prompt)
    return response.text

# Explain encrypted text
def explain_encryption(cipher_text):
    prompt = f"""You're an AI cryptography expert. Explain what this encrypted text might represent and how the encryption likely works:
    
    Encrypted data: {cipher_text}
    
    Give a simple, understandable explanation. If possible, guess the method (like AES or RSA)."""
    return ask_gemini(prompt)

# Translate content using AI
def translate_text(text, target_language):
    prompt = f"""Translate the following text into {target_language}:
    
    {text}
    
    Make sure it's accurate and culturally appropriate."""
    return ask_gemini(prompt)
