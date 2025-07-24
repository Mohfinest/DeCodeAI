import google.generativeai as genai
import streamlit as st

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-pro')

def explain_encryption(prompt_text):
    prompt = f"Explain the following encryption process in simple terms:\n{prompt_text}"
    response = model.generate_content(prompt)
    return response.text

def translate_text(text, target_language):
    prompt = f"Translate this into {target_language}:\n{text}"
    response = model.generate_content(prompt)
    return response.text

def summarize_chat(messages):
    chat_string = "\n".join([f"{msg['user']}: {msg['text']}" for msg in messages])
    prompt = f"Summarize this encrypted conversation:\n{chat_string}"
    response = model.generate_content(prompt)
    return response.text

def explain_code(code_snippet):
    prompt = f"Explain the following code in simple terms:\n{code_snippet}"
    response = model.generate_content(prompt)
    return response.text
