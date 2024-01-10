# Copyright 2023 Jiwon Park, Inigo Perez Gamiz

from bb84 import bb84_protocol
import aes

if __name__=="__main__":
    # Shared key generation using BB84 protocol
    quantum_key = bb84_protocol()
    if quantum_key == None:     # Check if the key was not generated
        raise ValueError("The key could not be generated due to an attemp of interception")
      
    # Convert the quantum key to bytes for AES encryption
    quantum_key_bytes = bytes((sum(b << i for i, b in enumerate(reversed(byte))) for byte in [quantum_key[i:i+8] for i in range(0, len(quantum_key), 8)]))   
        
    # Encrypt a message using AES
    message_to_encrypt = b"Hello, Quantum World!"
    encrypted_message = aes.aes_encrypt(message_to_encrypt, quantum_key_bytes)

    # Decrypt the message using AES
    decrypted_message = aes.aes_decrypt(encrypted_message, quantum_key_bytes)

    print(f"Original Message: {message_to_encrypt}")
    print(f"Encrypted Message: {encrypted_message}")
    print(f"Decrypted Message: {decrypted_message}")