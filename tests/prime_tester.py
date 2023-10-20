import unittest
from utils.key_generator import RSAKeyGeneratorService
from prime_checkers import SolovayStrassenTester, FermatTester, MillerRabinTester


def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    for f in range(5,r+1, 6):
        if n % f == 0: return False
        if n % (f+2) == 0: return False
    return True

class PrimalityTests(unittest.TestCase):


    def test_fermat_high_prob(self):
        keygen = RSAKeyGeneratorService(FermatTester())
        keygen.generate_keys(0.99,56)
        self.assertTrue(is_prime(keygen.p) and is_prime(keygen.q))

    def test_solovay_high_prob(self):
        keygen = RSAKeyGeneratorService(SolovayStrassenTester())
        keygen.generate_keys(0.99, 56)
        self.assertTrue(is_prime(keygen.p) and is_prime(keygen.q))

    def test_miller_high_prob(self):
        keygen = RSAKeyGeneratorService(MillerRabinTester())
        keygen.generate_keys(0.99, 56)
        self.assertTrue(is_prime(keygen.p) and is_prime(keygen.q))

    def test_fermat_low_prob(self):
        keygen = RSAKeyGeneratorService(FermatTester())
        keygen.generate_keys(0.5, 56)
        self.assertTrue(is_prime(keygen.p) and is_prime(keygen.q))

    def test_solovay_low_prob(self):
        keygen = RSAKeyGeneratorService(SolovayStrassenTester())
        keygen.generate_keys(0.5, 56)
        self.assertTrue(is_prime(keygen.p) and is_prime(keygen.q))

    def test_miller_low_prob(self):
        keygen = RSAKeyGeneratorService(MillerRabinTester())
        keygen.generate_keys(0.5, 56)
        self.assertTrue(is_prime(keygen.p) and is_prime(keygen.q))