#!/usr/bin/env python3
# File Encryption

from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()
cipher = Fernet(key)

# Save key to file
with open("secret.key", "wb") as key_file:
    key_file.write(key)

# Encrypt file
file_to_encrypt = "example.txt"
with open(file_to_encrypt, "rb") as f:
    data = f.read()
encrypted = cipher.encrypt(data)

with open(file_to_encrypt + ".enc", "wb") as f:
    f.write(encrypted)

print("[+] File encrypted successfully")
