import unittest
from simple_rsa import SimpleRSA

class TestSimpleRSA(unittest.TestCase):
    def test_gcd(self):
        rsa = SimpleRSA(61, 53, 17)
        self.assertEqual(rsa._gcd(48, 18), 6)
        self.assertEqual(rsa._gcd(101, 10), 1)
        self.assertEqual(rsa._gcd(0, 5), 5)
        self.assertEqual(rsa._gcd(5, 0), 5)
        self.assertEqual(rsa._gcd(270, 192), 6)

if __name__ == '__main__':
    unittest.main()