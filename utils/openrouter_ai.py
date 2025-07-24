import os
import requests
import streamlit as st
from utils.encryption import encrypt_text, decrypt_text
from utils.openrouter_ai import explain_encryption, translate_text

# Set page settings and branding header
st.set_page_config(page_title="DeCodeAI", page_icon="🔐")

st.markdown("""
    <div style='text-align: center;'>
        <h1>🔐 DeCodeAI</h1>
        <h3 style='color: gray;'>AI-Powered Encryption & Explanation Tool</h3>
        <p><strong>Built by MUSA HAMZA MUHAMMAD</strong></p>
    </div>
""", unsafe_allow_html=True)

# 🔐 Load API Key from environment variable (recommended for Streamlit secrets)
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# ✅ Define the model and endpoint
MODEL = "qwen/qwen3-8b:free"
API_URL = "https://openrouter.ai/api/v1/chat/completions"


# 💬 Sends a prompt to the OpenRouter API
def ask_openrouter(prompt):
    if not OPENROUTER_API_KEY:
        return "❌ Missing OpenRouter API key. Set OPENROUTER_API_KEY in Streamlit secrets."

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": MODEL,
        "messages": [
            { "role": "user", "content": prompt }
        ]
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()  # Raises exception for 4xx/5xx
        return response.json()['choices'][0]['message']['content']
    except requests.RequestException as req_err:
        return f"❌ Request error: {str(req_err)}"
    except (KeyError, IndexError) as parse_err:
        return f"❌ Response parsing error: {str(parse_err)}"


# 🔍 Ask LLM to explain an encryption snippet
def explain_encryption(code_snippet):
    prompt = f"Explain this encryption code clearly for a beginner:\n\n{code_snippet}"
    return ask_openrouter(prompt)


# 🌐 Ask LLM to translate text to a given language
def translate_text(text, target_language):
    prompt = f"Translate the following to {target_language}:\n\n{text}"
    return ask_openrouter(prompt)
    st.markdown("""---""")
st.markdown("""
    <div style='text-align: center; font-size: 14px;'>
        Made with ❤️ by <strong>MUSA HAMZA MUHAMMAD</strong><br>
        <a href="https://github.com/mohfinest" target="_blank">GitHub</a> |
        <a href="https://linkedin.com/in/YOUR-HANDLE" target="_blank">LinkedIn</a>
    </div>
""", unsafe_allow_html=True)
