## detecting fast-flux
## first we check if the packet has DNSRR if yes extract Rnam and rdata
## second we compare the domain name and ip agaisnt a dict
## if domain already exists we check the ip address if ip changed we change it
## if domain does ot exist we add it

from scapy.all import *

dnsRecord = {}

def handlePKT(pkt):
    if pkt.haslayer(DNSRR):
        # dns name
        rrname = pkt.getlayer(DNSRR).rrname
        # dns info such as ip addr
        rdata = pkt.getlayer(DNSRR).rdata
    if dnsRecord.has_key(rrname):
        if rdata not in dnsRecord[rrname]:
            dnsRecord[rname].append(rdata)
    else:
        dnsRecord[rrname]= []
        dnsRecord[rrname].append(rdata)

def main():
    pkts = rdpcap('.pcap')
    for pkt in pkts:
        handlePKT(pkt)
    for item in dnsRecord:
        print(f"[+] {item} has {str(len(dnsRecord[item]))} unique IPs")


if __name__ == '__main__':
    main()
