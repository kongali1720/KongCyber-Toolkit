#!/usr/bin/env python3
# Network Scanner (Ethical, ping scan)

import nmap

def scan_network(ip_range="192.168.1.0/24"):
    nm = nmap.PortScanner()
    print(f"[+] Scanning network: {ip_range}")
    nm.scan(hosts=ip_range, arguments='-sn')
    for host in nm.all_hosts():
        print(f"Host: {host}, Status: {nm[host].state()}")

if __name__ == "__main__":
    scan_network()
