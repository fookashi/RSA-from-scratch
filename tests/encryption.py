import unittest
from rsa.RSA import RSAEncryptionService
from rsa.utils.key_generator import RSAKeyGeneratorService
from prime_tester import SolovayStrassenTester

class EncryptionTests(unittest.TestCase):


    def test_small_plaintext(self):
        keygen = RSAKeyGeneratorService(SolovayStrassenTester())
        rsa = RSAEncryptionService(keygen, 0.99, 32)
        plaintext = b"hello"
        encrypted = rsa.encrypt(plaintext)
        self.assertEqual(rsa.decrypt(encrypted), plaintext)

    def test_empty_plaintext(self):
        keygen = RSAKeyGeneratorService(SolovayStrassenTester())
        rsa = RSAEncryptionService(keygen, 0.99, 32)
        plaintext = b""
        encrypted = rsa.encrypt(plaintext)
        self.assertEqual(rsa.decrypt(encrypted), b"")

    def test_plaintext_with_newlines(self):
        keygen = RSAKeyGeneratorService(SolovayStrassenTester())
        rsa = RSAEncryptionService(keygen, 0.99, 32)
        plaintext = b"fadgaga\nfasgfagfsdg\nfadskjag\ndfjafsd\n"
        encrypted = rsa.encrypt(plaintext)
        self.assertEqual(rsa.decrypt(encrypted), plaintext)