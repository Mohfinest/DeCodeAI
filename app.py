import streamlit as st
import os
from utils.encryption import encrypt_text, decrypt_text
from utils.openrouter_ai import explain_encryption, translate_text

# --- Page setup ---
st.set_page_config(page_title="🔐 DeCodeAI", layout="centered")

# --- App Header ---
st.markdown("""
    <div style='text-align: center;'>
        <h1>🔐 DeCodeAI</h1>
        <h3 style='color: gray;'>AI-Powered Encryption & Explanation Tool</h3>
        <p><strong>Built by MUSA HAMZA MUHAMMAD</strong></p>
    </div>
""", unsafe_allow_html=True)

# --- Sidebar menu ---
menu = st.sidebar.selectbox("Choose a feature", ["Encrypt", "Decrypt", "Explain Encryption", "Translate Text"])

# --- Encrypt Feature ---
if menu == "Encrypt":
    text = st.text_area("Enter text to encode (Base64)")
    if st.button("Encode"):
        encoded = encrypt_text(text)
        st.success("Encoded Text:")
        st.code(encoded)

# --- Decrypt Feature ---
elif menu == "Decrypt":
    encoded = st.text_area("Enter Base64-encoded text")
    if st.button("Decode"):
        try:
            decoded = decrypt_text(encoded)
            st.success("Decoded Text:")
            st.code(decoded)
        except Exception as e:
            st.error(f"Decoding failed: {e}")

# --- Explain Feature ---
elif menu == "Explain Encryption":
    code = st.text_area("Paste encryption code to explain")
    if st.button("Explain with AI"):
        with st.spinner("Thinking..."):
            result = explain_encryption(code)
        st.info("Explanation:")
        st.write(result)

# --- Translate Feature ---
elif menu == "Translate Text":
    text = st.text_area("Enter text to translate")
    lang = st.selectbox("Choose a language to translate to", ["Hausa", "Igbo", "Yoruba"])
    if st.button("Translate"):
        with st.spinner("Translating..."):
            translation = translate_text(text, lang)
        st.info("Translation:")
        st.write(translation)

# --- Footer ---
st.markdown("""---""")
st.markdown("""
    <div style='text-align: center; font-size: 14px;'>
        Made with ❤️ by <strong>MUSA HAMZA MUHAMMAD</strong><br>
        <a href="https://github.com/mohfinest" target="_blank">GitHub</a> |
        <a href="https://linkedin.com/in/YOUR-LINKEDIN" target="_blank">LinkedIn</a>
    </div>
""", unsafe_allow_html=True)
