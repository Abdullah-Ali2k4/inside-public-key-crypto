# Imagine a scenario where Bob, Alice, and Eve are three persons.
# Bob wants to send a message to Alice without letting Eve know its contents.

import public_key_crypto as p

# Alice generates a public-private key pair and shares her public key with everyone (including Bob and Eve).
Alice = p.Client()
alice_public_key = Alice.get_public_key()

# Bob uses Alice's public key to encrypt his message and sends the encrypted message to Alice.
Bob = p.Client()
secret_message = 50
encrypted_msg = Bob.encrypt(secret_message, alice_public_key)

# Eve intercepts the message and tries to decrypt it using Alice's public key (which is not possible).
Eve = p.Client()  # Eve is just another entity here, with her own keys

eve_attempt = Eve.decrypt(encrypted_msg)  # Will fail to get the correct result
print("Eve's attempt to decrypt the message:", eve_attempt)


# Alice receives the message and decrypts it using her private key.
bob_msg = Alice.decrypt(encrypted_msg)
print("Decrypted message from Bob:", bob_msg)

# Alice signs a message (e.g., 1000) using her private key.
signature = Alice.add_signature(1000)

# Bob (or anyone, including Eve) can verify that the message was signed by Alice using her public key.
verify_by_bob = Bob.check_signature(signature, alice_public_key)
verify_by_eve = Eve.check_signature(signature, alice_public_key)

print("Verified signature result by Bob:", verify_by_bob)
print("Verified signature result by Eve:", verify_by_eve)

