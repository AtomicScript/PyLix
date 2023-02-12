from struct import *
import socket, sys
import binascii


def ethernet_head(raw_data):
    dest, src, prototype = unpack('!6s6s2s', raw_data[:14])
    # Binary to hex
    dest_mac = dest
    src_mac = src
    proto = prototype
    data = raw_data[14:]
    return dest_mac, src_mac, proto, data

# INET raw socket = IPV4, SOCK_RAW : RAW SOCKET; IPPROTO_TCP is the Protocol
# THIS ENABLES RAW DATA
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)

while True:
    # recv means that it recieves all data from the socket in hex
    raw_data, addr = s.recvfrom(65565)
    eth = ethernet_head(raw_data)
    print('\nEthernet Frame:')
    print(f'Destination: {eth[0]}, Source: {eth[1]}, Protocol: {eth[2]}')
    print(f'Data: {eth[3]}')
