# 🔐 RSA Client-Server Secure Communication

A comprehensive Python implementation demonstrating secure client-server communication using RSA public-key cryptography. This project simulates real-world secure communication protocols like SSH, TLS, and PGP with complete encryption, authentication, and digital signature capabilities.

## 🎯 Overview

This system implements a complete RSA-based communication framework where clients and servers can securely exchange messages without ever sharing private keys. The implementation covers all three pillars of information security:

- **🔒 Confidentiality**: Messages are encrypted so only intended recipients can read them
- **✅ Authentication**: Digital signatures prove the sender's identity  
- **🛡️ Integrity**: Recipients can verify messages haven't been tampered with

## 🚀 Quick Start

```python
import public_key_crypto as p

# Basic encryption example
alice = p.Client()
bob = p.Client()

# Alice shares her public key
alice_public = alice.get_public_key()

# Bob encrypts a message for Alice
encrypted = bob.encrypt(42, alice_public)

# Alice decrypts Bob's message
decrypted = alice.decrypt(encrypted)
print(f"Bob's message: {decrypted}")  # Output: 42
```

## 📁 Project Structure

```
rsa-communication/
├── 📄 public_key_crypto.py     # Core RSA classes (Client/Server)
├── 🔧 helper.py               # Utility functions (primes, GCD)
├── 👥 Bob-Alice.py            # 3-party communication demo
├── 🔄 secure_tunneling.py     # Full bidirectional communication
├── 📚 rsa_math_explained.md   # Mathematical foundations
└── 📖 README.md              # This file
```

## 🏗️ Core Components

### Client Class
The main class that handles RSA operations:

```python
class Client:
    def __init__(self)                          # Auto-generates RSA key pair
    def get_public_key(self)                    # Returns (e, n) tuple
    def encrypt(self, msg, public_key)          # Encrypt with recipient's key
    def decrypt(self, msg)                      # Decrypt with own private key
    def add_signature(self, msg)                # Create digital signature
    def check_signature(self, msg, public_key)  # Verify signature
```

### Server Class
Extends Client with server-specific functionality:

```python
class Server(Client):
    def give_key(self)  # Provides public key to requesting clients
```

## 📖 Usage Examples

### Example 1: Bob-Alice-Eve Scenario

This demonstrates the classic cryptography scenario where Bob wants to send a secret message to Alice while preventing Eve from reading it:

```python
import public_key_crypto as p

# Alice generates keys and makes public key available
alice = p.Client()
alice_public_key = alice.get_public_key()

# Bob encrypts his message using Alice's public key
bob = p.Client()
secret_message = 50
encrypted_msg = bob.encrypt(secret_message, alice_public_key)

# Alice decrypts the message with her private key
decrypted_msg = alice.decrypt(encrypted_msg)
print("Bob's secret message:", decrypted_msg)

# Alice creates a digital signature to prove authenticity
signature = alice.add_signature(1000)

# Anyone can verify Alice signed this message using her public key
verified = bob.check_signature(signature, alice_public_key)
print("Alice's verified message:", verified)
```

### Example 2: Full Client-Server Communication

This shows a complete secure communication setup with key exchange and authenticated messaging:

```python
import public_key_crypto as p

server = p.Server()
client = p.Client()

# Phase 1: Client requests server's public key
server_public_key = client.request(server)
client.set_store_public_key(server_public_key)

# Client sends encrypted message to server
encrypted_msg = client.encrypt(400, server_public_key)
server_received = server.decrypt(encrypted_msg)
print("Server received:", server_received)

# Phase 2: Secure key exchange (client shares its public key)
client_public_key = client.get_public_key()

# Client encrypts its own public key using server's public key
encrypted_key = (
    client.encrypt(client_public_key[0], server_public_key),
    client.encrypt(client_public_key[1], server_public_key)
)

# Server decrypts and stores client's public key
decrypted_key = (
    server.decrypt(encrypted_key[0]),
    server.decrypt(encrypted_key[1])
)
server.set_store_public_key(decrypted_key)

# Phase 3: Authenticated communication
signed_message = client.add_signature(1200)
encrypted_signed = client.encrypt(signed_message, server_public_key)

decrypted_signed = server.decrypt(encrypted_signed)
verified_message = server.check_signature(decrypted_signed, decrypted_key)
print("Verified authentic message:", verified_message)
```

## 🔬 How It Works

### RSA Key Generation
1. Generate two random prime numbers `p` and `q`
2. Calculate modulus `n = p × q`
3. Calculate Euler's totient `φ(n) = (p-1)(q-1)`
4. Choose public exponent `e` coprime to `φ(n)`
5. Calculate private exponent `d` where `e × d ≡ 1 (mod φ(n))`

### Encryption Process
- **Encrypt**: `ciphertext = message^e mod n`
- **Decrypt**: `message = ciphertext^d mod n`

### Digital Signatures
- **Sign**: `signature = message^d mod n` (private key)
- **Verify**: `message = signature^e mod n` (public key)

## 🌍 Real-World Applications

| Technology | How This Project Relates |
|------------|-------------------------|
| **SSH** | Public key authentication, secure shell access |
| **TLS/SSL** | HTTPS website security, certificate verification |
| **PGP/GPG** | Email encryption, file signing |
| **Digital Certificates** | Code signing, document authenticity |
| **Blockchain** | Transaction signing, wallet security |

## 🛡️ Security Features

### ✅ What This Implementation Provides
- **Public-key cryptography** fundamentals
- **Digital signature** creation and verification  
- **Key exchange** without pre-shared secrets
- **Message authentication** and integrity checking
- **Educational insight** into cryptographic protocols

### ⚠️ Educational Limitations
- Small key sizes (not production-ready)
- Basic prime generation (not cryptographically secure)
- No padding schemes (vulnerable to certain attacks)
- Simplified implementation for learning purposes

### 🔒 Production Recommendations
For real applications, use:
- **Larger keys** (2048+ bits minimum)
- **Cryptographic libraries** (OpenSSL, cryptography)
- **Proper padding** (OAEP for encryption, PSS for signatures)
- **Secure random** number generation

## 🎓 Learning Path

1. **Start with mathematical foundations** → Read `rsa_math_explained.md`
2. **Basic encryption** → Run `Bob-Alice.py`
3. **Full communication** → Explore `secure_tunneling.py`
4. **Implementation details** → Study `public_key_crypto.py`
5. **Helper functions** → Understand `helper.py`

## 🚦 Getting Started

### Prerequisites
- Python 3.6 or higher
- Basic understanding of modular arithmetic (helpful but not required)

### Running the Examples
```bash
# Basic 3-party demonstration
python Bob-Alice.py

# Complete client-server communication
python secure_tunneling.py

# Interactive exploration
python3
>>> import public_key_crypto as p
>>> client = p.Client()
>>> print(client.get_public_key())
```

## 🤝 Contributing

Contributions welcome! Ideas for improvement:

- **Enhanced Security**: Implement proper padding schemes
- **Performance**: Optimize prime generation and exponentiation
- **Features**: Add key serialization, network communication
- **Documentation**: More examples and use cases
- **Testing**: Comprehensive test suite

## 📚 Additional Resources

- **Mathematical Background**: See `rsa_math_explained.md` for detailed mathematical explanations
- **RSA Algorithm**: [Wikipedia - RSA Cryptosystem](https://en.wikipedia.org/wiki/RSA_(cryptosystem))

## ⚠️ Important Notice

**This is an educational implementation.** Do not use in production systems. For real-world applications requiring security, use established, audited cryptographic libraries and follow current security best practices.

---

*🔐 "In cryptography we trust, but we verify the math."*
