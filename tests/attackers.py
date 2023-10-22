import unittest
from rsa.attacks import FermatAttacker, WienerAttacker
from rsa.keygen.key_generator import RSAKeyGeneratorService
from rsa.prime_checkers import FermatTester
from rsa.numgen.number_generator import NumberGenerator


class TestAttacks(unittest.TestCase):

    def setUp(self) -> None:
        key_gen = RSAKeyGeneratorService(FermatTester(), NumberGenerator())
        self.public_key, self.private_key = key_gen.generate_keys(0.99,32)
    def test_fermat_attacker(self):
        attacker = FermatAttacker()
        d = attacker.attack(self.public_key)
        self.assertEqual(d, self.private_key.d)

    def test_wiener_attacker(self):
        attacker = WienerAttacker()
        d = attacker.attack(self.public_key)
        self.assertEqual(d, self.private_key.d)
