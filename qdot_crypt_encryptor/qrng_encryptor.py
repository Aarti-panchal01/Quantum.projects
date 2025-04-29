import base64
import numpy as np
from cryptography.fernet import Fernet

def generate_qrng_key():
    # Generate a 32-byte base64-encoded key using QD-inspired randomness
    random_bytes = np.random.bytes(32)
    key = base64.urlsafe_b64encode(random_bytes)
    return key

def encrypt_message(message, key):
    f = Fernet(key)
    encrypted = f.encrypt(message.encode())
    return encrypted

def decrypt_message(encrypted_message, key):
    f = Fernet(key)
    decrypted = f.decrypt(encrypted_message).decode()
    return decrypted

if __name__ == "__main__":
    key = generate_qrng_key()
    print("Generated Quantum RNG-based Key:", key.decode())

    msg = input("Enter your message: ")
    encrypted = encrypt_message(msg, key)
    print("Encrypted Message:", encrypted.decode())

    decrypted = decrypt_message(encrypted, key)
    print("Decrypted Message:", decrypted)
