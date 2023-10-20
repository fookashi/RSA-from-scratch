from interfaces import IRSAKeyGenerator, IRSAEncrypter
import math

class RSAEncryptionService(IRSAEncrypter):

    def __init__(self, key_generator: IRSAKeyGenerator, min_prob: float, key_length: int):
        self.key_generator = key_generator
        self.public_key, self.private_key = self.key_generator.generate_keys(min_prob, key_length)

    def encrypt(self, data: str):
        msg_ciphertext = [pow(ord(c), self.public_key.e, self.public_key.n) for c in data]
        return msg_ciphertext

    def decrypt(self, data: str):

        msg_plaintext = [chr(pow(c, self.private_key.d, self.private_key.n)) for c in data]
        # No need to use ord() since c is now a number
        # After decryption, we cast it back to character
        # to be joined in a string for the final result
        return ''.join(msg_plaintext)

