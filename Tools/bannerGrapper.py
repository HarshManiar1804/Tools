# Banner Graper

# !/usr/bin/env python3

import socket

def findBanner(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(2)
            sock.connect((ip, port))
            banner = sock.recv(1024)
            return banner
    except:
        return None

def main():
    ip = input("Enter the IP to get the banner: ")
    for port in range(1, 100):
        banner = findBanner(ip, port)
        if banner:
            print(f"[*] {ip}/{port}: {banner.decode().strip()}")

if _name_ == "_main_":

    main()