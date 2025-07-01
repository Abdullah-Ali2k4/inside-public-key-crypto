import helper as h  # Assume helper has methods like get_prime() and GCD()

class Client:
    def __init__(self):
        # Generate and set the public/private key pair on initialization
        self._set_public_key()

    def set_store_public_key(self, public_key):
        # Store another party's public key for encrypting messages to them
        self.stored_public_key = public_key

    def get_store_public_key(self):
        # Retrieve the stored public key (of another client/server)
        return self.stored_public_key

    def _set_public_key(self):
        # Generate public and private keys using RSA algorithm
        p, q = h.get_prime(), h.get_prime()  # Get two random prime numbers
        self.n = p * q                       # n = modulus for public/private key
        self.phi = (p - 1) * (q - 1)         # φ(n) = totient of n
        
        # Find a suitable public exponent 'e' that is coprime with φ(n)
        self.e = 0
        for i in range(2, self.phi):
            if h.GCD(i, self.phi):           # Check if i and φ(n) are coprime
                self.e = i                   # Assign i to e
                break

        # Compute the private exponent 'd' such that (e * d) % φ(n) = 1
        self._set_d()

    def get_public_key(self):
        # Return the public key as a tuple (e, n)
        return (self.e, self.n)

    def _set_d(self):
        # Find d using a brute-force method to satisfy (e * d) % φ(n) == 1
        i = 1
        while True:
            if (self.e * i) % self.phi == 1:
                self.d = i  # private exponent
                break
            i += 1

    def decrypt(self, msg):
        # Decrypt the message using the private key: msg^d % n
        decrypted = (msg ** self.d) % self.n
        return decrypted

    def add_signature(self, msg):
        # Create a digital signature by "encrypting" with private key: msg^d % n
        signatured = (msg ** self.d) % self.n
        return signatured

    def encrypt(self, msg, public_key):
        # Encrypt the message using the recipient's public key: msg^e % n
        (e, n) = public_key
        encrypted = (msg ** e) % n
        return encrypted

    def check_signature(self, msg, public_key):
        # Verify a digital signature using sender’s public key: msg^e % n
        (e, n) = public_key
        signature_key = (msg ** e) % n
        return signature_key

    def request(self, Server):
        # Ask the server to provide its public key
        return Server.give_key()

# Server inherits from Client — same functionality with extra behavior
class Server(Client):

    def give_key(self):
        # Return this server's public key
        return (self.e, self.n)




