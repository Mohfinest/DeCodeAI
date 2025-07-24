import Crypto.Cipher  # <-- if it crashes here, it's still not installed
import streamlit as st
from utils.encryption import encrypt_aes, decrypt_aes
from utils.gemini_ai import explain_encryption, translate_text, summarize_chat, explain_code

st.set_page_config(page_title="Encryptify AI", layout="wide")
st.title("🔐 Encryptify AI – Smart Encryption Toolkit")

st.sidebar.title("⚙️ Options")
mode = st.sidebar.radio("Choose Mode", ["Encrypt/Decrypt", "AI Explain", "Translate", "Secure Chat", "Code Explainer"])

# Store chat session
if "chat_messages" not in st.session_state:
    st.session_state.chat_messages = []

# ENCRYPTION / DECRYPTION
if mode == "Encrypt/Decrypt":
    st.subheader("🔏 AES Encryption / Decryption")

    text = st.text_area("Enter text", height=150)
    key = st.text_input("Enter a 16-char key")
    action = st.radio("Action", ["Encrypt", "Decrypt"])

    if st.button("Run"):
        if not key or len(key) < 16:
            st.warning("Key must be at least 16 characters.")
        elif action == "Encrypt":
            result = encrypt_aes(text, key)
            st.success("Encrypted text:")
            st.code(result)
        else:
            try:
                result = decrypt_aes(text, key)
                st.success("Decrypted text:")
                st.code(result)
            except Exception as e:
                st.error(f"Decryption failed: {e}")

# AI EXPLAIN
elif mode == "AI Explain":
    st.subheader("🤖 Explain This Encryption")

    raw = st.text_area("Paste your encrypted text, or describe your process:")
    if st.button("Explain with Gemini"):
        with st.spinner("Thinking..."):
            explanation = explain_encryption(raw)
            st.success("Gemini says:")
            st.write(explanation)

# TRANSLATION
elif mode == "Translate":
    st.subheader("🌍 Translate Text with Gemini")
    txt = st.text_area("Enter text to translate")
    lang = st.text_input("Translate to (e.g., French, Hausa, Yoruba, Igbo, Spanish)")

    if st.button("Translate"):
        with st.spinner("Translating..."):
            translated = translate_text(txt, lang)
            st.success("Translation:")
            st.write(translated)

# SECURE CHAT
elif mode == "Secure Chat":
    st.subheader("💬 Encrypted Chat + AI Summary")

    user = st.text_input("Name", value="You")
    msg = st.text_input("Your message")
    key = st.text_input("Encryption key (16 chars)", key="chatkey")

    if st.button("Send"):
        encrypted = encrypt_aes(msg, key)
        st.session_state.chat_messages.append({"user": user, "text": encrypted})
        st.success("Encrypted message sent!")

    for chat in st.session_state.chat_messages:
        st.write(f"**{chat['user']}**: `{chat['text']}`")

    if st.button("Summarize Chat with Gemini"):
        summary = summarize_chat(st.session_state.chat_messages)
        st.info("Gemini's Summary:")
        st.write(summary)

# CODE EXPLAINER
elif mode == "Code Explainer":
    st.subheader("🧠 Code Explanation")

    code = st.text_area("Paste your AES or RSA code here")
    if st.button("Explain Code"):
        with st.spinner("Gemini is analyzing..."):
            explanation = explain_code(code)
            st.success("Gemini says:")
            st.write(explanation)
