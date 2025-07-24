import os
import requests

# Load OpenRouter API key from Streamlit Secrets
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL = "qwen/qwen3-8b:free"
API_URL = "https://openrouter.ai/api/v1/chat/completions"

def ask_openrouter(prompt):
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

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        try:
            return response.json()['choices'][0]['message']['content']
        except Exception as e:
            return f"❌ Response parsing error: {str(e)}"
    else:
        return f"❌ API error {response.status_code}: {response.text}"

def explain_encryption(code_snippet):
    prompt = f"Explain this encryption code clearly for a beginner:\n\n{code_snippet}"
    return ask_openrouter(prompt)

def translate_text(text, target_language):
    prompt = f"Translate the following to {target_language}:\n\n{text}"
    return ask_openrouter(prompt)
