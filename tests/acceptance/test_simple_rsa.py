import unittest
from simple_rsa import SimpleRSA

class TestSimpleRSA(unittest.TestCase):
    def setUp(self):
        # Initialize with small prime numbers for testing
        self.rsa = SimpleRSA(61, 53, 17)

    def test_public_key(self):
        self.assertEqual(self.rsa.public_key, (61 * 53, 17))

    def test_private_key(self):
        self.assertEqual(self.rsa.private_key[0], 61 * 53)
        self.assertTrue(self.rsa.private_key[1] > 0)

    def test_encrypt_decrypt(self):
        plaintext = "hello"
        encrypted = self.rsa.encrypt(plaintext)
        decrypted = self.rsa.decrypt(encrypted)
        self.assertEqual(decrypted, plaintext)

    def test_mod_inverse(self):
        self.assertEqual(self.rsa._mod_inverse(17, (61 - 1) * (53 - 1)), self.rsa.private_key[1])

if __name__ == '__main__':
    unittest.main()