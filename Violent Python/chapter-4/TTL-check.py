from scapy.all import *
from IPy import IP as IPTEST
import time
import optparse

ttl_Valued = {}
Thresh = 5


def testTTL(pkt):
    try:
        # checks if its an IP
        if pkt.haslayer(IP):
            # gets the source address
            ipsrc = pkt.getlayer(IP).src
            # gets the ttl of that address
            ttl = str(pkt.ttl)
            print(f"[+] Packet recieved from {ipsrc} with TTL: {ttl}")
            checkTTL(ipsrc, ttl)
    except:
        pass


def checkTTL(ipsrc, ttl):
    # first we need to check if its a private ip to ignore them
    if IPTEST(ipsrc).iptype() == 'PRIVATE':
        return

    if not ttl_Valued.has_key(ipsrc):
        # send a packet to src to add the ttl value of that src
        pkt = sr1(IP(dst=ipsrc) / ICMP(), retry=0, timeout=1, verbose=0)
        ttl_Valued[ipsrc] = pkt.ttl

    if abs(int(ttl) - int(ttl_Valued[ipsrc])) > THRESH:
        print(f"[!] Detected Possible Spoofed Packet from: {ipsrc}")
        print(f"[!] TTL: {ttl} , Actual TTL: {str(ttlValues[ipsrc])}")



def main():
    parser = optparse.OptionParser("usage%prog -i<interface> -t <thresh>")
    parser.add_option('-i', dest='iface', type='string', help='specify network interface')
    parser.add_option('-t', dest='thresh', type='int', help='specify thresh count')
    (options, args) = parser.parse_args()
    if options.iface == None:
        conf.iface = 'ens33'
    else:
        conf.iface = options.iface
    if options.thresh == None:
        THRESH = conf.thresh
    else:
        THRESH = 5

    sniff(prn=testTTL, store=0)


if __name__ == '__main__':
    main()
