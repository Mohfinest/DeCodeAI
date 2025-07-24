from Crypto.Cipher import AES 
import base64

def pad(text):
    while len(text) % 16 != 0:
        text += ' '
    return text

def encrypt_aes(text, key):
    key = key[:16].encode('utf-8')  # AES requires 16-byte key
    text = pad(text).encode('utf-8')
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted = cipher.encrypt(text)
    return base64.b64encode(encrypted).decode()

def decrypt_aes(ciphertext, key):
    key = key[:16].encode('utf-8')
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted = cipher.decrypt(base64.b64decode(ciphertext))
    return decrypted.decode().strip()
