from rsa.interfaces import IRSAKeyGenerator, IRSAEncrypter
import math
from rsa.utils.transform import int2bytes, bytes2int
from pathlib import Path

class RSAEncryptionService(IRSAEncrypter):

    def __init__(self, key_generator: IRSAKeyGenerator, min_prob: float, key_length: int):
        self.key_generator = key_generator
        self.key_length = key_length
        self.public_key, self.private_key = self.key_generator.generate_keys(min_prob, key_length)

    def encrypt(self, data: bytes):
        if len(data) * 8 <= self.key_length:
            ciphertext = pow(bytes2int(data), self.public_key.e, self.public_key.n)
            ciphertext = int2bytes(ciphertext)
        else:
            ciphertext = bytearray()
            block_size = self.key_length // 8 # Размер блока

            for i in range(0, len(data), block_size):
                block = data[i:i + block_size]
                ciphertext_block = pow(bytes2int(block), self.public_key.e, self.public_key.n)
                ciphertext_block = int2bytes(ciphertext_block)
                ciphertext += ciphertext_block

        return ciphertext

    def decrypt(self, data: bytes):
        if len(data) * 8 <= self.key_length:
            plaintext = pow(bytes2int(data), self.private_key.d, self.private_key.n)
            plaintext = int2bytes(plaintext)
        else:
            plaintext = bytearray()
            block_size = self.key_length // 8  # Размер блока

            for i in range(0, len(data), block_size):
                block = data[i:i + block_size]
                plaintext_block = pow(bytes2int(block), self.private_key.d, self.private_key.n)
                plaintext_block = int2bytes(plaintext_block)
                plaintext += plaintext_block

        return plaintext

    def encrypt_file(self, input_path: str, output_path: str, chunk_size: int):
        with open(Path(output_path), 'wb') as out_f:
            with open(Path(input_path), 'rb') as inp_f:
                while chunk := inp_f.read(chunk_size):
                    ciphered = self.encrypt(chunk)
                    out_f.write(ciphered)

    def decrypt_file(self, input_path: str, output_path: str, chunk_size: int):
        with open(Path(output_path), 'wb') as out_f:
            with open(Path(input_path), 'rb') as inp_f:
                while chunk := inp_f.read(chunk_size):
                    deciphered = self.decrypt(chunk)
                    out_f.write(deciphered)