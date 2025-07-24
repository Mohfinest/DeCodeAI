import os
import requests
from utils.encryption import encrypt_text, decrypt_text

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
