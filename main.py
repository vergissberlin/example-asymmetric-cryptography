from simple_rsa import SimpleRSA

# Beispiel für die Verwendung der SimpleRSA-Klasse
if __name__ == "__main__":
    # Primzahlen und öffentlicher Exponent
    p = 61
    q = 53
    e = 17

    # Instanz der SimpleRSA-Klasse erstellen
    rsa = SimpleRSA(p, q, e)

    # Nachricht zum Verschlüsseln
    message = "Hello"
    print(f"Originalnachricht: {message}")

    # Verschlüsseln
    encrypted_message = rsa.encrypt(message)
    print(f"Verschlüsselter Text: {encrypted_message}")

    # Entschlüsseln
    decrypted_message = rsa.decrypt(encrypted_message)
    print(f"Entschlüsselte Nachricht: {decrypted_message}")
