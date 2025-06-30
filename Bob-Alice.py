# Imagine a scenario where Bob, Alice, and Eve are three persons.
# Bob wants to send a message to Alice without letting Eve know its contents.

import public_key_crypto as p

# Alice generates a public-private key pair and shares her public key with everyone (including Bob and Eve).
Alice = p.Client()
public_key = Alice.get_public_key()

# Bob uses Alice's public key to encrypt his message and sends the encrypted message to Alice.
Bob = p.Client()
encrypted_msg = Bob.encrypt(50, public_key)

# Alice receives the message and decrypts it using her private key.
bob_msg = Alice.decrypt(encrypted_msg)
print("Decrypted message from Bob:", bob_msg)

# Alice signs a message (for example, 1000) using her private key.
signature = Alice.add_signature(1000)

# Bob (or anyone, including Eve) can verify that the message was signed by Alice using Alice's public key.
verify = Bob.check_signature(signature, public_key)
print("Verified signature result:", verify)
