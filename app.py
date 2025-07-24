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
    text = st.text_area("Enter text to encrypt")
    key = st.text_input("Enter a secret key (16/24/32 characters)", type="password")

    if st.button("Encrypt"):
        key = key.strip()
        key_length = len(key)

        if key_length not in [16, 24, 32]:
            st.error(f"❌ Key must be 16, 24, or 32 characters. You entered {key_length} characters.")
        else:
            encrypted = encrypt_text(text, key)
            st.success("🔒 Encrypted Text:")
            st.code(encrypted)

# --- Decrypt Feature ---
elif menu == "Decrypt":
    encrypted = st.text_area("Enter encrypted text")
    key = st.text_input("Enter the same secret key", type="password")

    if st.button("Decrypt"):
        key = key.strip()
        key_length = len(key)

        if key_length not in [16, 24, 32]:
            st.error(f"❌ Key must be 16, 24, or 32 characters. You entered {key_length} characters.")
        else:
            try:
                decrypted = decrypt_text(encrypted, key)
                st.success("🔓 Decrypted Text:")
                st.code(decrypted)
            except Exception as e:
                st.error(f"Decryption failed: {e}")

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
    lang = st.text_input("Translate to (e.g. French, Yoruba, Spanish)")
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
