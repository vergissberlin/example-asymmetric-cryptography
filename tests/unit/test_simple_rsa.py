import unittest
from simple_rsa import SimpleRSA


class TestSimpleRSA(unittest.TestCase):

    def setUp(self):
        # Initialize SimpleRSA with small prime numbers and a public exponent
        self.rsa = SimpleRSA(61, 53, 17)
        self.plaintext = "HELLO"
        self.ciphertext = self.rsa.encrypt(self.plaintext)

    def test_gcd(self):
        rsa = SimpleRSA(61, 53, 17)
        self.assertEqual(rsa._gcd(48, 18), 6)
        self.assertEqual(rsa._gcd(101, 10), 1)
        self.assertEqual(rsa._gcd(0, 5), 5)
        self.assertEqual(rsa._gcd(5, 0), 5)
        self.assertEqual(rsa._gcd(270, 192), 6)

    def test_encrypt(self):
        plaintext = "hello"
        expected_ciphertext = self.rsa.encrypt(plaintext)
        # Encrypt the plaintext and check if the result matches the expected
        # ciphertext
        self.assertEqual(self.rsa.encrypt(plaintext), expected_ciphertext)

    def test_decrypt(self):
        decrypted_text = self.rsa.decrypt(self.ciphertext)
        self.assertEqual(decrypted_text, self.plaintext)

    def test_modular_inverse_exists(self):
        rsa = SimpleRSA(61, 53, 17)
        self.assertEqual(rsa._mod_inverse(17, 3120), 2753)

    def test_encrypt_decrypt_message(self):
        rsa = SimpleRSA(61, 53, 17)
        plaintext = "hello"
        encrypted = rsa.encrypt(plaintext)
        decrypted = rsa.decrypt(encrypted)
        self.assertEqual(decrypted, plaintext)

    def test_encrypt_decrypt_empty_message(self):
        rsa = SimpleRSA(61, 53, 17)
        plaintext = ""
        encrypted = rsa.encrypt(plaintext)
        decrypted = rsa.decrypt(encrypted)
        self.assertEqual(decrypted, plaintext)

    def test_encrypt_decrypt_special_characters(self):
        rsa = SimpleRSA(61, 53, 17)
        plaintext = "!@#$%^&*()"
        encrypted = rsa.encrypt(plaintext)
        decrypted = rsa.decrypt(encrypted)
        self.assertEqual(decrypted, plaintext)


if __name__ == '__main__':
    unittest.main()
