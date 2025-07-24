from Crypto.Cipher import AES
import base64

def encrypt_aes(text, key):
    combined = f"{key}:{text}"
    encoded = base64.b64encode(combined.encode()).decode()
    return encoded

def decrypt_aes(encoded_text, key):
    decoded = base64.b64decode(encoded_text.encode()).decode()
    decoded_key, message = decoded.split(":", 1)
    if decoded_key == key:
        return message
    else:
        return "❌ Incorrect decryption key!"
# AES Decryption Function
def decrypt_aes(encrypted_text, key):
    key = pad_key(key).encode()
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted = cipher.decrypt(base64.b64decode(encrypted_text.encode()))
    pad = decrypted[-1]
    return decrypted[:-pad].decode()
