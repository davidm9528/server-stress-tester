import logging

from scapy.layers.inet import IP, UDP
from scapy.sendrecv import sr1
logging.getLogger("Scapy.runtime").setLevel(logging.ERROR)
import time
import sys

if len(sys.argv) != 4:
    print("Usage: scanner.py <ip> <startport> <end-port>")
    sys.exit()

ip=sys.argv[1]
start=int(sys.argv[[2]])
end=int(sys.argv[3])

for port in range(start, end):
    ans=sr1(IP(dst=ip)/UDP(dport=port), timeout=5, verbose=0)
    if ans==None:
        print(port)
    else:
        pass