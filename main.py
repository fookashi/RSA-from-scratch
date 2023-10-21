from RSA import RSAEncryptionService
from utils.key_generator import RSAKeyGeneratorService
from prime_checkers import SolovayStrassenTester, FermatTester, MillerRabinTester
from attacks import FermatAttacker, WienerAttacker



def process_file():
    key_generator = RSAKeyGeneratorService(FermatTester())
    rsa = RSAEncryptionService(key_generator, 0.99, 64)
    rsa.encrypt_file("file.txt", "ciphered.txt", 32)
    rsa.decrypt_file("ciphered.txt", "decrypted.txt", 32)
def process_plaintext():
    key_generator = RSAKeyGeneratorService(SolovayStrassenTester())
    rsa = RSAEncryptionService(key_generator, 0.99, 128)
    plaintext = b"HELLOHELLOHELLOHELLOHELLOHELLOHELLOHELLOHELLOHELLOHELLOHELLOHELLOHELLOHELLOHELLOHELLOHELLOHELLOHELLOHELLOHELLOHELLOHELLOHELLOHELLOHELLOHELLOHELLOHELLOHELLOHELLOHELLOHELLOHELLOHELLOHELLOHELLOHELLOHELLOHELLOHELLOHELLOHELLO"
    ciphered = rsa.encrypt(plaintext)
    decrypted = rsa.decrypt(ciphered)
    print(f"Исходный текст: {plaintext}")
    print(f"Зашифрованный текст: {ciphered.hex()}")
    print(f"Расшифрованный текст: {decrypted}")
def attack():
    key_generator = RSAKeyGeneratorService(FermatTester())
    rsa = RSAEncryptionService(key_generator, 0.99, 56)
    fermat_d = FermatAttacker().attack(rsa.public_key)
    wiener_d = WienerAttacker().attack(rsa.public_key)
    print(f"Сгенерированный d: {rsa.private_key.d}")
    print(f"Полученный атакой ферма: {fermat_d}")
    print(f"Полученный атакой винера: {wiener_d}")

def main():
    attack()
if __name__ == "__main__":
    main()