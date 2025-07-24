import base64

def encrypt_aes(text, key):
    """
    Fake AES-style encryption using base64 for demo purposes.
    Combines key and message, then encodes it.
    """
    combined = f"{key}:{text}"
    encoded = base64.b64encode(combined.encode()).decode()
    return encoded

def decrypt_aes(encoded_text, key):
    """
    Fake AES-style decryption.
    Decodes base64 and checks if key matches.
    """
    try:
        decoded = base64.b64decode(encoded_text.encode()).decode()
        decoded_key, message = decoded.split(":", 1)
        if decoded_key == key:
            return message
        else:
            return "❌ Incorrect decryption key!"
    except Exception as e:
        return f"❌ Decryption failed: {str(e)}"
