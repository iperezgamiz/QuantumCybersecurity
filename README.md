# QUANTUM COMPUTING AND CYBERSECURITY
EC601 A2 Team 3

## Motivation
The emergence of Quantum Computation has completely changed the computational landscape, specially in terms of cybersecurity. Many encryption algorithms that
for years have been considered to be safe against classical computers, now confront potential vulnerabilities in the face of quantum computers. Their security relies on the difficulty for classical computers to efficiently solve certain mathematical operations. However, with the development of some quantum algorithms, the complexity of these problems is considerably reduced. This is the case of asymmetric encryption methods, like the famous RSA, that are mainly threatened by Shor’s quantum algorithm. RSA is based on factorizing prime numbers, and trusts its effectiveness to the fact that a classical computer needs exponential time to perform this operation. According to Shor, a quantum computer can factorize a number in polynomial time, which means that RSA is absolutely vulnerable against these computers. In a similar fashion but to a lesser extent, Grover’s algorithm affects symmetric encryption methods (for instance, AES). Grover proved that the number of brute force attempts needed to break a symmetric encryption key can be reduced to the square root using a quantum computer. Even though it is a considerable complexity reduction, it can not be compared to the one offered by Shor’s Algorithm for asymmetric encryption methods. 

In this context, our project proposes 2 safe solutions against quantum computers:

- **Communication protocol simulator based on BB84 and AES:** robust simulator for the secure transmission of data between two parties. A shared key is generated using the BB84 Quantum Key Distribution protocol (Quantum Mechanics based), and this key is later used to encrypt and decrypt data with the symmetric AES method.
- **QuantumGuard Chatbot: Next-Gen Encrypted Messaging with Kyber and ChatGPT**: innovative chatbot implementation that leverages the power of Kyber512 post-quantum key encapsulation method and ChatGPT for a next-generation encrypted communication experience. The chatbot is an application of the cybersecurity system; it could be applied in other contexts.


## Product Mission
Make cybersecurity professionals aware of the risk that quantum computers suppose for classical encryption algorithms, providing them with 2 safe alternatives: one based on Quantum Key Distribution, and the other on Post-quantum cryptography.

## Users
- Cybersecurity professionals, including researchers (private companies, universities, government) and engineers (private companies and public institutions)
- Cybersecurity enthusiasts

## User Stories and MVP
1. I, cybersecurity professional, want a solution that takes advantage of the capabilities of quantum mechanics. <code style="color : greenyellow">Now</code>
2. I, cybersecurity professional, want an encryption system that protects classical computers againt quantum computers. <code style="color : greenyellow">Now</code>
3. I, cybersecurity professional, want to have the chance to test the encryption systems. <code style="color : greenyellow">Now</code>
4. I, cybersecurity researcher, want a good explanation of the concepts to be able to expand them in the future. <code style="color : greenyellow">Now</code>
5. I, cybersecurity researcher, want a source code for encryption algorithms to take it as a reference for further developments. <code style="color : greenyellow">Now</code>
6. I cybersecurity engineer, want an interface that allows me to manage the encryption of data and check if it is working. <code style="color : greenyellow">Later</code>
7. I, cybersecurity engineer, want a way to contact a support team in case there were issues. <code style="color : greenyellow">Now</code>
8. I, cybersecurity enthusiast, want an open source code of the encryption methods to have the chance to study them and potentially contribute to their improvement. <code style="color : greenyellow">Later</code>

## Further Information
For additional information about the products, please refer to the respective README files for each of them.  
[BB84_AES_README](https://github.com/Jpark99/Quantum_Security/blob/main/BB84_AES_sim/README.md)  
[QuantumGuard_ChatBot_README](https://github.com/Jpark99/Quantum_Security/blob/main/QuantumGuard_ChatBot/README.md)

## Contact support
Jiwon Park: jiwon327@bu.edu   
Inigo Perez Gamiz: iperezg@bu.edu
