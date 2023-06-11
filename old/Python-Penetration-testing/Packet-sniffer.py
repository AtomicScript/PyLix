from struct import *
import socket, sys
import binascii


def ethernet_head(raw_data):
    # means first 6 bytes dest, Next 6 bytes src and H for htons ! space is important
    dest, src, prototype = unpack('! 6s 6s H', raw_data[:14])
    # Binary to hex
    dest_mac = ":".join("{:d}".format(int(x, 16)) for x in dest.hex().split(':'))
    src_mac = ":".join("{:d}".format(int(x, 16)) for x in src.hex().split(':'))
    proto = socket.htons(prototype)
    data = raw_data[14:]
    return dest_mac, src_mac, proto, data

# INET raw socket = IPV4, SOCK_RAW : RAW SOCKET; IPPROTO_TCP is the Protocol
# THIS ENABLES RAW DATA
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)

while True:
    # recv means that it recieves all data from the socket in hex
    raw_data, addr = s.recvfrom(65565)
    print(addr)
    eth = ethernet_head(raw_data)
    print('\nEthernet Frame:')
    print(f'Destination: {eth[0]}, Source: {eth[1]}, Protocol: {eth[2]}')
    print(f'Data: {eth[3]}')
