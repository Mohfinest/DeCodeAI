import os
import requests

# 🔐 Load API Key from environment variable
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
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
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content']
    except requests.RequestException as req_err:
        return f"❌ Request error: {str(req_err)}"
    except (KeyError, IndexError) as parse_err:
        return f"❌ Response parsing error: {str(parse_err)}"

# 🔍 Explain code
def explain_encryption(code_snippet):
    prompt = f"Explain this encryption code clearly for a beginner:\n\n{code_snippet}"
    return ask_openrouter(prompt)

# 🌐 Translate
def translate_text(text, target_language):
    prompt = f"Translate the following to {target_language}:\n\n{text}"
    return ask_openrouter(prompt)
