MACchanger


#!/usr/bin/env python3

import subprocess

def change_mac(interface, mac):
    subprocess.call(["sudo", "ifconfig", interface, "down"])
    subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", mac])
    subprocess.call(["sudo", "ifconfig", interface, "up"])

def main():
    interface = input("Enter the interface: ")
    # interface = "eth0"
    new_mac_address = input("Enter the new MAC address: ")

    before_change = subprocess.check_output(["ifconfig", interface])
    change_mac(interface, new_mac_address)
    after_change = subprocess.check_output(["ifconfig", interface])

    if before_change == after_change:
        print("[-] MAC address not changed")
    else:
        print("[+] MAC address is changed")

if _name_ == "_main_":
    main()