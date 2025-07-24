import streamlit as st
from utils.encryption import encrypt_text, decrypt_text
from utils.openrouter_ai import explain_encryption, translate_text

st.set_page_config(page_title="🔐 DeCodeAI", layout="centered")

st.title("🔐 DeCodeAI – AI-Powered Encryption & Explanation Tool")

menu = st.sidebar.selectbox("Choose a feature", ["Encrypt", "Decrypt", "Explain Encryption", "Translate Text"])

# --- Encrypt
if menu == "Encrypt":
    text = st.text_area("Enter text to encrypt")
    key = st.text_input("Enter a secret key (16/24/32 characters)", type="password")
    if st.button("Encrypt"):
        if len(key) not in [16, 24, 32]:
            st.error("Key must be 16, 24, or 32 characters.")
        else:
            encrypted = encrypt_text(text, key)
            st.success("Encrypted Text:")
            st.code(encrypted)

# --- Decrypt
elif menu == "Decrypt":
    encrypted = st.text_area("Enter encrypted text")
    key = st.text_input("Enter the same secret key", type="password")
    if st.button("Decrypt"):
        try:
            decrypted = decrypt_text(encrypted, key)
            st.success("Decrypted Text:")
            st.code(decrypted)
        except Exception as e:
            st.error(f"Decryption failed: {e}")

# --- Explain Encryption
elif menu == "Explain Encryption":
    code = st.text_area("Paste encryption code to explain")
    if st.button("Explain with AI"):
        with st.spinner("Thinking..."):
            result = explain_encryption(code)
        st.info("Explanation:")
        st.write(result)

# --- Translate
elif menu == "Translate Text":
    text = st.text_area("Enter text to translate")
    lang = st.text_input("Translate to (e.g. French, Yoruba, Spanish)")
    if st.button("Translate"):
        with st.spinner("Translating..."):
            translation = translate_text(text, lang)
        st.info("Translation:")
        st.write(translation)
