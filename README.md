# Asymmetric cryptography example for beginners

[![.github/workflows/tests.yml](https://github.com/vergissberlin/example-asymmetric-cryptography/actions/workflows/tests.yml/badge.svg)](https://github.com/vergissberlin/example-asymmetric-cryptography/actions/workflows/tests.yml)

Example to asymmetric cryptography beginners. This example is a simple way to understand how asymmetric cryptography works.
With this example, you can understand how to generate a public and private key, encrypt and decrypt a message.
It uses the RSA algorithm to encrypt and decrypt the message. It is implemented in Python.
It does not use any library to generate the keys, encrypt and decrypt the message. 
It is implemented from scratch.

## How to run

1. Clone the repository
2. Run the following command to install the dependencies:
```bash
pip install -r requirements.txt
```
3. Run the following command to execute the code:
```bash
python main.py
```

## Testing

To test the code, run the following command:
```bash
python -m unittest discover -s tests -p "test_*.py"
```
