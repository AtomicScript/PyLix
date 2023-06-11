# identify domain-flux by identifying all the DNS responses
# that contains error code for name error
from scapy.all import *

def dnsQRtest(pkt):
    if pkt.haslayer(DNSRR) and pkt.getlayer(UDP).sport == 53:
        rcode = pkt.getlayer(DNS).rcode
        qname = pkt.getlayer(DNSQR).qname

        if rcode ==3:
            print(f"[!] Error: Name request lookup failed of : {qname}")
            return True
        else:
            return False

def main():
    unAnsReqs = 0
    pkts = rdpcap('.pcap')
    for pkt in pkts:
        if dnsQRtest(pkt):
            unAnsReqs+=1
    print(f"[!] {str(unAnsReqs)} Total Unanswered Name Requests")

if __name__ == '__main__':
    main()
