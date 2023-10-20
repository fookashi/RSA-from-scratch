import math
import time

from RSA import RSAEncryptionService
from utils.key_generator import RSAKeyGeneratorService
from prime_checkers import SolovayStrassenTester, FermatTester, MillerRabinTester
from attacks.fermat import FermatAttacker

def encrypt():


    
    key_generator = RSAKeyGeneratorService(FermatTester())
    rsa = RSAEncryptionService(key_generator, 0.99, 16)
    from utils.newton_sq_root import isqrt as newton_sq_root
    import math
    t1 = time.time()
 
    print('KEY GENERATED')
    
    plaintext = "Hello world Hello world Hello world Hello world Hello world Hello world"
    
    encrypted = rsa.encrypt(plaintext)
    decrypted= rsa.decrypt(encrypted)
    
    
    print(f"Исходный текст: {plaintext}")
    print(f"Зашифрованный текст: {encrypted}")
    print(f"Дешифрованный текст: {decrypted}")
    
    
    attacked_d = FermatAttacker().attack(rsa.public_key.n, rsa.public_key.e)
    print(f"d полученный атакой: {attacked_d}, исходный d: {rsa.private_key.d}")
    
    t2=time.time()
    print(t2-t1)
    return
def main():
    encrypt()
if __name__ == "__main__":
    main()