<h1 align="center"> QuantumGuard ChatBot:<br/>  Next-Gen Encrypted Messaging with Kyber and ChatGPT </h1>

## Description
QuantumGuard ChatBot is a secure and innovative chatbot implementation that leverages the power of Kyber512 encapsulation and ChatGPT for a next-generation encrypted communication experience. Quantum computers are a real threat to classical computers in terms of cybersecurity. While some solutions are being developed based on Quantum Mechanics, as it is the key of Quantum Key Distribution, classical computers need new cybersecurity systems that protect them from quantum algorithms. This is the main purpose of post-quantum cryptography, to build classical encryption methods that are resistant against quantum computers. One of the post-quantum methods that the NIST is trying to standarize is Kyber, a key encapsulation algorithm that is based on the problem of Learning With Errors (LWE). In this project, we combine Kyber together with AES to enable messaging between the user and the bot.   

## Features
- **Server-client communication:** between the user (client) and the bot (server).
- **Shared Key Generation:** Utilize the Kyber512 encapsulation method to generate shared keys between server and client, ensuring a robust encryption foundation based on the Learning With Errors (LWE) lattice problem.

- **AES Encryption:** Encrypt and decrypt messages using the generated key through the Advanced Encryption Standard (AES) method.

- **ChatBot's Responses:** ChatBot's responses are generated using the OpenAI API.

## Key Generation: Kyber512

The key is generated using Kyber512 asymmetric (or public-key) method. The steps are the following:

1. Initially, the server generates a pair of public and private keys using Kyber512 key generation, and posts the public key for everyone.
2. The client takes the public key and encapsulates it using Kyber512 encapsulation. The result is a private key and a ciphertext containing the private key. This ciphertext is sent to the server.
3. The server receives the ciphertext and decapsulates it to obtain the private key shared with the client. 

Kyber is a Post-Quantum Key Encapsualtion Method (PQ-KEM), resistant to quantum computers. It is based on Learning with Errors (Lattice) problem, which is not efficiently solvable by any quantum algorithm for now. To learn more about Kyber or PQ-KEM, take a look here: [Deep dive into a post-quantum key encapsulation algorithm](https://blog.cloudflare.com/post-quantum-key-encapsulation/)

![image](https://github.com/Jpark99/Quantum_Security/assets/10427379/00cd9bf7-794d-424d-a32a-e14660a7c50f)

_(source: [Deep dive into a post-quantum key encapsulation algorithm](https://blog.cloudflare.com/post-quantum-key-encapsulation/) by Goutam Tamvada and Sofía Celi on The Cloudflare Blog)_

## AES Encryption
AES is a classical symmetric method for the encryption of data. It requires a shared private key between the sender and the receiver to encrypt and decrypt data. AES is resistant against quantum computers, since Grover's algorithm only presents a square-root speedup over classical brute force algorithm to force keys. In this product, the key used for AES is the one generated using Kyber.

## Usage Guide

How to clone the repository:
```bash
git clone https://github.com/Jpark99/Quantum_Security/
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Before runing the program, replace "YOUR-OPENAI-API-KEY" in server.py with your OpenAI API key.

To run the ChatBot, open two command line terminals. In one of them, run the program <code style="color : greenyellow">server.py</code>:
```bash
python server.py
```
In the other terminal, run <code style="color : greenyellow">client.py</code>:
```bash
python client.py
```

In terminal, you will see if the shared key was successfully generated. In case it was, start chatting!

To exit, simply type in "exit" or "Exit".

## Example

**Server Side**

![serverphoto](https://github.com/Jpark99/Quantum_Security/assets/10427379/b96ff7ca-4034-4fae-8160-38fa520a91e0)

**User Side**
  
![clientphoto](https://github.com/Jpark99/Quantum_Security/assets/10427379/dee9285a-8222-405c-8444-4e23cb441153)


