import unittest
from RSA import RSAEncryptionService
from utils.key_generator import RSAKeyGeneratorService
from prime_tester import SolovayStrassenTester

class EncryptionTests(unittest.TestCase):


    def test_small_plaintext(self):
        keygen = RSAKeyGeneratorService(SolovayStrassenTester())
        rsa = RSAEncryptionService(keygen, 0.99, 10)
        plaintext = "hello"
        encrypted = rsa.encrypt(plaintext)
        self.assertEqual(rsa.decrypt(encrypted), plaintext)

    def test_empty_plaintext(self):
        keygen = RSAKeyGeneratorService(SolovayStrassenTester())
        rsa = RSAEncryptionService(keygen, 0.99, 10)
        plaintext = ""
        encrypted = rsa.encrypt(plaintext)
        self.assertEqual(rsa.decrypt(encrypted), plaintext)

    def test_plaintext_with_newlines(self):
        keygen = RSAKeyGeneratorService(SolovayStrassenTester())
        rsa = RSAEncryptionService(keygen, 0.99, 10)
        plaintext = "fadgaga\nfasgfagfsdg\nfadskjag\ndfjafsd\n"
        encrypted = rsa.encrypt(plaintext)
        self.assertEqual(rsa.decrypt(encrypted), plaintext)