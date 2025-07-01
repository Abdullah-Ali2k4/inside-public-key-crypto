import public_key_crypto as p

# Create instances of Server and Client
server = p.Server()
client = p.Client()

# ========== PHASE 1: Secure Client → Server Communication ==========

# Step 1: Client requests the public key of the server
public_keyS = client.request(server)

# Step 2: Client stores the server's public key for encryption
client.set_store_public_key(public_keyS)

# Step 3: Client encrypts the message (e.g., 400) using server's public key
encrypted_msg = client.encrypt(400, client.get_store_public_key())

# Step 4: Server receives the encrypted message and decrypts it using its private key
decrypt_msg = server.decrypt(encrypted_msg)

# Output the decrypted message on the server side
print(decrypt_msg)  # Should print: 400

# ========== PHASE 2: Secure Server → Client Communication ==========

# Step 1: Client shares its public key (which is a tuple like (e, n))
public_keyC = client.get_public_key()

# Step 2: Client encrypts each part of its own public key using the server's public key
# This ensures only the server can decrypt and use this public key securely
encrypt_key = (
    client.encrypt(public_keyC[0], client.get_store_public_key()),  # e
    client.encrypt(public_keyC[1], client.get_store_public_key())   # n
)

# Step 3: Server decrypts the encrypted key parts using its private key
decrypted_key = (
    server.decrypt(encrypt_key[0]),
    server.decrypt(encrypt_key[1])
)

# Step 4: Server stores the client’s public key for future encryption
server.set_store_public_key(decrypted_key)

# ========== PHASE 3: Authenticated Client → Server Message ==========

# Step 1: Client signs the message (e.g., 1200) using its private key
# This adds a digital signature that proves authenticity
client_msg = client.add_signature(1200)

# Step 2: Client encrypts the signed message with the server’s public key (for confidentiality)
encrypted_client_msg = client.encrypt(client_msg, client.get_store_public_key())

# Step 3: Server decrypts the encrypted signed message using its private key
client_sign = server.decrypt(encrypted_client_msg)

# Step 4: Server verifies the digital signature using the client’s public key (it stored earlier)
msg = server.check_signature(client_sign, server.get_store_public_key())

# Output the original verified message
print(msg)  # Should print: 1200 if signature is valid
