# Copyright 2023 Jiwon Park, Inigo Perez Gamiz

"""
kyber imported from repository https://github.com/GiacomoPope/kyber-py
MIT License, Copyright (c) 2022 Giacomo Pope
"""

import socket
from kyber import Kyber512
import aes


def client_encapsulate(server_public_key):
    client_ciphertext, shared_key = Kyber512.enc(server_public_key)
    return client_ciphertext, shared_key


def client_run():
    # 2. Client connects to server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    # 5. Client gets server's public key and encapsulates it using Kyber512
    # to generate shared private key. This shared private key
    # is sent as ciphertext to the server
    server_public_key = client_socket.recv(1024)
    print("Server's public key received")
    client_ciphertext, shared_key = client_encapsulate(server_public_key)
    client_socket.sendall(client_ciphertext)

    # 7. Client receives from server if the key generation was successful
    # In case it was, the conversation starts
    encrypted_update = client_socket.recv(1024)
    update = aes.aes_decrypt(encrypted_update, shared_key)
    if update != "Key exchange successful!":
        print("Key exchange NOT successful!")
        return 0
    print("Key exchange successful!")
    # Conversation starts
    print("Start your conversation")
    message = str(input("You: "))
    # Messages are encrypted using AES
    encrypted_message = aes.aes_encrypt(message, shared_key)
    if message == "exit" or message == "Exit":
        client_socket.sendall(encrypted_message)
        return 0
    client_socket.sendall(encrypted_message)

    while True:
        encrypted_response = client_socket.recv(1024)
        response = aes.aes_decrypt(encrypted_response, shared_key)
        print("Bot: ", response)
        message = str(input("You: "))
        # The conversation is ended when the user types exit
        if message == "exit" or message == "Exit":
            break
        encrypted_message = aes.aes_encrypt(message, shared_key)
        client_socket.sendall(encrypted_message)

    encrypted_message = aes.aes_encrypt(message, shared_key)
    client_socket.sendall(encrypted_message)

    return 0


if __name__ == "__main__":
    client_run()
