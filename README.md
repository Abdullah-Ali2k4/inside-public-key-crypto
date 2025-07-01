## 🔁 Client–Server RSA Communication

This project simulates a secure client-server communication model using RSA public-key cryptography. Both the `Client` and `Server` generate their own public-private key pairs. Communication between them is encrypted, authenticated, and verified without sharing private keys.

---

### 💡 Objectives

- Ensure **confidentiality**: Only the intended recipient can read the message.
- Ensure **authentication**: The sender proves their identity through digital signatures.
- Ensure **integrity**: The receiver can verify that the message was not tampered with.

---

### 🧱 Process Overview

#### 1. Client to Server
- The client obtains the server's public key.
- It encrypts and sends messages securely to the server.

#### 2. Server to Client
- The client sends its own public key to the server (securely).
- The server stores the client's public key for future verification.

#### 3. Digital Signature Exchange
- The client signs messages using its private key.
- The server verifies the signature using the client's stored public key.

---

### 🧠 Real-World Analogy

This RSA-based communication pattern mimics how secure systems like **SSH**, **TLS**, and **PGP** operate:

| Real System            | This Project Simulates              |
|------------------------|-------------------------------------|
| SSH public key login   | Client key stored on server         |
| TLS handshake          | Mutual key exchange and encryption  |
| Digital certificates   | Public key verification and trust   |

---

### 📄 Related Files

| File                 | Purpose                                        |
|----------------------|------------------------------------------------|
| `public_key_crypto.py` | Core logic for RSA key generation and use     |
| `Bob-Alice.py`       | Demonstrates full communication process        |
| `secure_tunneling.py`| Implements bi-directional secured messaging    |
