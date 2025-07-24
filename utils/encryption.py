from Crypto.Cipher import AES
import base64

# Helper function to ensure key is 16 bytes long
def pad_key(key):
    return key.ljust(16)[:16]

# AES Encryption Function
def encrypt_aes(text, key):
    key = pad_key(key).encode()
    cipher = AES.new(key, AES.MODE_ECB)
    padded_text = text + (16 - len(text) % 16) * chr(16 - len(text) % 16)
    encrypted = cipher.encrypt(padded_text.encode())
    return base64.b64encode(encrypted).decode()

# AES Decryption Function
def decrypt_aes(encrypted_text, key):
    key = pad_key(key).encode()
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted = cipher.decrypt(base64.b64decode(encrypted_text.encode()))
    pad = decrypted[-1]
    return decrypted[:-pad].decode()
