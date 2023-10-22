from rsa.interfaces import IRSAKeyGenerator, IPrimalityTester, INumberGenerator
from rsa.utils.mod_inverser import ModInverser
from rsa.keys import RSAPrivateKey, RSAPublicKey
from rsa.numgen.number_generator import NumberGenerator


class RSAKeyGeneratorService(IRSAKeyGenerator):
    def __init__(self, prime_checker: IPrimalityTester, number_generator: INumberGenerator):
        self.mod_inverser = ModInverser()
        self.prime_checker = prime_checker
        self.number_generator = number_generator
        self.p = None
        self.q = None



    def generate_keys(self, min_probability: float, key_length: int):
        if key_length % 8 != 0:
            raise ValueError("Key length must be power of 2 and more or equal 8")

        while p := self.number_generator.generate_number(key_length//2):
            if self.prime_checker.is_prime(p, min_probability):
                break

        while q := self.number_generator.generate_number(key_length//2):
            if self.prime_checker.is_prime(q, min_probability):
                break

        self.p, self.q = p, q
        n = self.p * self.q
        phi_n = (self.p - 1) * (self.q - 1)
        e = 65537
        d = self.mod_inverser.calculate_mod_inverse(e, phi_n)
        public_key = RSAPublicKey(n, e)
        private_key = RSAPrivateKey(n, d)

        return public_key, private_key
