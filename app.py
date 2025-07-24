import streamlit as st
from utils.encryption import encrypt_aes, decrypt_aes
from utils.gemini_ai import explain_encryption, translate_text

st.set_page_config(page_title="DeCodeAI", layout="centered")
st.title("🔐 DeCodeAI – AI-powered Encryption & Explanation")

# Input form
with st.form("encryption_form"):
    text = st.text_area("🔤 Enter text to encrypt:")
    password = st.text_input("🔑 Enter encryption key:", type="password")
    submitted = st.form_submit_button("Encrypt")

if submitted and text and password:
    encrypted = encrypt_aes(text, password)
    st.success("✅ Encrypted Text:")
    st.code(encrypted)

    if st.button("🔍 Explain Encryption"):
        explanation = explain_encryption(encrypted)
        st.info("🧠 Gemini Explanation:")
        st.write(explanation)

    if st.button("🌍 Translate to French"):
        translated = translate_text(text, "French")
        st.success("🌐 Translated:")
        st.write(translated)

# Optional decryption
with st.expander("🔓 Decrypt Text"):
    enc_input = st.text_input("Enter encrypted text")
    key_input = st.text_input("Enter encryption key", type="password")
    if st.button("Decrypt"):
        result = decrypt_aes(enc_input, key_input)
        st.code(result)
