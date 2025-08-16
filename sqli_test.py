#!/usr/bin/env python3
# Basic SQL Injection Testing (Ethical)

import requests

urls = ["http://example.com/page?id=1"]
payloads = ["'", '"', "' OR '1'='1", '" OR "1"="1']

for url in urls:
    for payload in payloads:
        try:
            r = requests.get(url + payload, timeout=5)
            if "sql" in r.text.lower():
                print(f"[!] SQLi Potential: {url + payload}")
            else:
                print(f"[-] Safe: {url + payload}")
        except Exception as e:
            print(f"[-] Error testing {url + payload}: {e}")
