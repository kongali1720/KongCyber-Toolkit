#!/usr/bin/env python3
# File Decryption

from cryptography.fernet import Fernet

# Load key
with open("secret.key", "rb") as key_file:
    key = key_file.read()

cipher = Fernet(key)

# Decrypt file
file_to_decrypt = "example.txt.enc"
with open(file_to_decrypt, "rb") as f:
    encrypted_data = f.read()

decrypted = cipher.decrypt(encrypted_data)

with open("example_decrypted.txt", "wb") as f:
    f.write(decrypted)

print("[+] File decrypted successfully")
