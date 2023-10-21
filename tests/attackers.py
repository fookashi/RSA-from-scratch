import unittest
from rsa.keys import RSAPublicKey
from rsa.attacks import FermatAttacker, WienerAttacker
from rsa.utils.key_generator import RSAKeyGeneratorService
from rsa.prime_checkers import FermatTester

class TestRSAAttacks(unittest.TestCase):

    def setUp(self) -> None:
        self.public_key, self.private_key = RSAKeyGeneratorService(FermatTester()).generate_keys(0.99,32)
    def test_fermat_attacker(self):
        attacker = FermatAttacker()
        d = attacker.attack(self.public_key)
        self.assertEqual(d, self.private_key.d)

    def test_wiener_attacker(self):
        attacker = WienerAttacker()
        d = attacker.attack(self.public_key)
        self.assertEqual(d, self.private_key.d)


if __name__ == '__main__':
    unittest.main()
