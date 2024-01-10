# Copyright 2023 Jiwon Park, Inigo Perez Gamiz

"""
kyber imported from repository https://github.com/GiacomoPope/kyber-py
MIT License, Copyright (c) 2022 Giacomo Pope
"""

import socket
import aes
from kyber import Kyber512


def server_key_generation():
    server_public_key, server_private_key = Kyber512.keygen()
    return server_public_key, server_private_key


def server_decapsulate(client_ciphertext, server_private_key):
    decrypted_shared_key = Kyber512.dec(client_ciphertext, server_private_key)
    return decrypted_shared_key


import requests


def chatgpt_answer(message, api_key="YOUR-OPENAI-API-KEY", engine="text-davinci-002"):
    url = f"https://api.openai.com/v1/engines/{engine}/completions"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    data = {
        "prompt": message,
        "max_tokens": 150,
        "temperature": 0.7,
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()["choices"][0]["text"].strip()
    else:
        print("Error:", response.status_code)
        print(response.text)
        return None


def server_run():
    # 1. Server initializes connection and waits for clients
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 12345))
    server.listen(1)
    print("Server is listening...")

    # 3. Server accepts connection from client
    connection, address = server.accept()
    print(f"Connection from {address}")

    # 4. Server generates pair of public and private keys
    # and posts public key
    server_public_key, server_private_key = server_key_generation()
    print("Server has generated keys.")
    print("Server's public key posted: " + server_public_key.hex())
    connection.sendall(server_public_key)

    # 6. Server receives shared key as ciphertext and decapsulates it
    # using Kyber512 and its initial private key. Then notifies client
    # if the key generation was successful
    client_ciphertext = connection.recv(1024)
    print("Client's ciphertext received.")
    shared_key = server_decapsulate(client_ciphertext, server_private_key)
    print("Key exchange successful!")
    msg = "Key exchange successful!"
    connection.send(aes.aes_encrypt(msg, shared_key))

    while True:
        encrypted_message = connection.recv(1024)
        message = aes.aes_decrypt(encrypted_message, shared_key)
        print("User's message: ", message)
        # The conversation is ended when the user types exit
        if message == "exit" or message == "Exit":
            break
        response = chatgpt_answer(message)
        encrypted_response = aes.aes_encrypt(response, shared_key)
        connection.sendall(encrypted_response)

    return 0


if __name__ == "__main__":
    server_run()
