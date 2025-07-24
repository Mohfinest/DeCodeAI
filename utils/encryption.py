import base64

def encrypt_text(text: str) -> str:
    encoded = base64.b64encode(text.encode('utf-8')).decode('utf-8')
    return encoded

def decrypt_text(encoded_text: str) -> str:
    decoded = base64.b64decode(encoded_text.encode('utf-8')).decode('utf-8')
    return decoded
