from Crypto.Cipher import AES
import base64
import hashlib

def pad(text):
    pad_len = AES.block_size - len(text) % AES.block_size
    return text + chr(pad_len) * pad_len

def unpad(text):
    return text[:-ord(text[-1])]

def encrypt_text(plain_text, secret_key):
    key = hashlib.sha256(secret_key.encode()).digest()
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted = cipher.encrypt(pad(plain_text).encode())
    return base64.b64encode(encrypted).decode()

def decrypt_text(cipher_text, secret_key):
    key = hashlib.sha256(secret_key.encode()).digest()
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted = cipher.decrypt(base64.b64decode(cipher_text))
    return unpad(decrypted.decode())
