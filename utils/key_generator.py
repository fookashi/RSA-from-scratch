from interfaces import IRSAKeyGenerator, IPrimalityTester
from secrets import randbits
from .mod_inverser import ModInverser
from keys import RSAPrivateKey, RSAPublicKey
import math
from random import randint

class RSAKeyGeneratorService(IRSAKeyGenerator):
    def __init__(self, prime_checker: IPrimalityTester):
        self.mod_inverser = ModInverser()
        self.prime_checker = prime_checker
        self.p = None
        self.q = None

    def generate_keys(self, min_probability: float, key_length: int):
        while p := randbits(key_length):
            if p % 2 == 0:
                p += 1
            if self.prime_checker.is_prime(p, min_probability):
                break
        while q := randbits(key_length):
            if q % 2 == 0:
                q += 1
            if self.prime_checker.is_prime(q, min_probability):
                break
        self.p, self.q = p, q
        n = self.p * self.q
        phi_n = (self.p - 1) * (self.q - 1)
        # Генерируем открытый и закрытый ключи RSA
        e = 65537
        d = self.mod_inverser.calculate_mod_inverse(e, phi_n)

        public_key = RSAPublicKey(n, e)
        private_key = RSAPrivateKey(n, d)

        return public_key, private_key
