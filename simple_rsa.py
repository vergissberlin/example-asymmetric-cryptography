class SimpleRSA:
    def __init__(self, p, q, e):
        self.p = p  # Erste Primzahl
        self.q = q  # Zweite Primzahl
        self.n = p * q  # n = p * q
        self.phi = (p - 1) * (q - 1)  # phi(n)
        self.e = e  # Öffentlicher Exponent
        self.d = self._mod_inverse(e, self.phi)  # Privater Exponent

        # Öffentlicher und privater Schlüssel
        self.public_key = (self.n, self.e)
        self.private_key = (self.n, self.d)

    # Hilfsfunktion zur Berechnung des größten gemeinsamen Teilers (GCD)
    def _gcd(self, a, b) -> int:
        while b != 0:
            a, b = b, a % b
        return a

    # Erweiterter Euklidischer Algorithmus zur Berechnung des modularen Inversen
    def _mod_inverse(self, e, phi) -> int:
        def egcd(a, b)-> tuple[int, int, int]:
            if a == 0:
                return b, 0, 1
            else:
                g, x, y = egcd(b % a, a)
                return g, y - (b // a) * x, x

        g, x, y = egcd(e, phi)
        if g != 1:
            raise Exception('Modular inverse does not exist')
        else:
            return x % phi

    # Verschlüsselungsfunktion (m^e % n)
    def encrypt(self, plaintext) -> list[int]:
        n, e = self.public_key
        encrypted = [(ord(char) ** e) % n for char in plaintext]
        return encrypted

    # Entschlüsselungsfunktion (c^d % n)
    def decrypt(self, ciphertext) -> str:
        n, d = self.private_key
        decrypted = [chr((char ** d) % n) for char in ciphertext]
        return ''.join(decrypted)
