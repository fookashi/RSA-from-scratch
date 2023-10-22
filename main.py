from RSA import RSAEncryptionService
from rsa.keygen.key_generator import RSAKeyGeneratorService
from prime_checkers import MillerRabinTester, SolovayStrassenTester, FermatTester
from attacks import FermatAttacker, WienerAttacker
from rsa.numgen.number_generator import NumberGenerator



def process_file():
    key_generator = RSAKeyGeneratorService(FermatTester(), NumberGenerator())
    rsa = RSAEncryptionService(key_generator, 0.99, 1024)
    rsa.encrypt_file("file.txt", "ciphered.shit", 128)
    rsa.decrypt_file("ciphered.shit", "decrypted.txt", 128)
def process_plaintext():
    key_generator = RSAKeyGeneratorService(MillerRabinTester(), NumberGenerator())
    rsa = RSAEncryptionService(key_generator, 0.8, 128)
    plaintext = b"HELLOHELLOHELLOHELLOHELLOHELLOHELLOHELLOHELLOHELLOHELLOHELLOHELLOHELLOHELLOHELLOHELLOHELLOHELLOHELLOHELLOHELLOHELLOHELLOHELLOHELLOHELLOHELLOHELLOHELLOHELLOHELLOHELLOHELLOHELLOHELLOHELLOHELLOHELLOHELLOHELLOHELLOHELLOHELLO"
    ciphered = rsa.encrypt(plaintext)
    decrypted = rsa.decrypt(ciphered)
    print(f"Исходный текст: {plaintext}")
    print(f"Зашифрованный текст: {ciphered.hex()}")
    print(f"Расшифрованный текст: {decrypted}")
def attack():
    key_generator = RSAKeyGeneratorService(FermatTester(), NumberGenerator())
    rsa = RSAEncryptionService(key_generator, 0.99, 56)
    fermat_d = FermatAttacker().attack(rsa.public_key)
    wiener_d = WienerAttacker().attack(rsa.public_key)
    print(f"Сгенерированный d: {rsa.private_key.d}")
    print(f"Полученный атакой ферма: {fermat_d}")
    print(f"Полученный атакой винера: {wiener_d}")

def main():
    process_plaintext()
if __name__ == "__main__":
    main()