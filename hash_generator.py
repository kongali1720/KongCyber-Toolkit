#!/usr/bin/env python3
# Hash Generator (MD5, SHA1, SHA256)

import hashlib

text = input("Enter text to hash: ")

md5_hash = hashlib.md5(text.encode()).hexdigest()
sha1_hash = hashlib.sha1(text.encode()).hexdigest()
sha256_hash = hashlib.sha256(text.encode()).hexdigest()

print(f"MD5: {md5_hash}")
print(f"SHA1: {sha1_hash}")
print(f"SHA256: {sha256_hash}")
