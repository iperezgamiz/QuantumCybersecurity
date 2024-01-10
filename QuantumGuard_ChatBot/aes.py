# Copyright 2023 Jiwon Park, Inigo Perez Gamiz

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding


def aes_encrypt(message, key):
    # Convert the message to bytes
    message_bytes = message.encode('utf-8')

    # Ensure the message is a multiple of the block size by adding PKCS7 padding
    padder = padding.PKCS7(128).padder()
    padded_message = padder.update(message_bytes) + padder.finalize()

    # AES encryption implementation
    cipher = Cipher(algorithms.AES(key), modes.ECB())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_message) + encryptor.finalize()

    return ciphertext


def aes_decrypt(ciphertext, key):
    cipher = Cipher(algorithms.AES(key), modes.ECB())
    decryptor = cipher.decryptor()
    decrypted_message = decryptor.update(ciphertext) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    try:
        original_message = unpadder.update(decrypted_message) + unpadder.finalize()
        return original_message.decode('utf-8')  # Assuming the original message was a string
    except ValueError:
        # Invalid padding
        print("Error: Invalid padding bytes.")
        return None
