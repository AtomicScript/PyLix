from scapy.all import *
import sys

interface = 'wlx00871a051ce0'
devices = set()

# PROTOCOL
def packetHandler(pkt):
    # Dot11 =  Wireless LAN
    if pkt.haslayer(Dot11):
        dot11_layer = pkt.getlayer(Dot11)

    if dot11_layer.addr2 and (dot11_layer.addr2 not in devices):
        devices.add(dot11_layer.addr2)
        print(len(devices), dot11_layer.addr2, dot11_layer.payload.name)



sniff(iface=interface, count=100, prn=packetHandler)
