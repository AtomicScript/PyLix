import scapy.all as scapy

interface = 'wlx00871a051ce0'

request = scapy.ARP()

print("###[ Summary ]### ")
print(request.summary())

print("###[ Show ]### ")
print(request.show())

print("###[ LS ]### ")
print(scapy.ls(scapy.ARP()))
