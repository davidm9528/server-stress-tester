import socket
from socket import *
import string
import time

# pyshark

# scapy - Using this (I think)
"""sumary_line
from scapy.all import wrpcap, Ether, IP, UDP
packet = Ether() / IP(dst="127.0.0.1") / UDP(dport=1010)
wrpcap('foo.pcap', [packet])
"""

ip = "127.0.0.1"
port = 1010

serverudp = socket(AF_INET, SOCK_DGRAM)

# Connect with above IP and Port
serverudp.connect((ip, port))

# formatting
print("\n")
print("-" * 60)
print("client.py")
print("-" * 60)
print("Starting client, press ctrl+c to end.")
print("\nTarget: ")

print("server.py running on %s port %s" % (ip, port))
print("-" * 60)

checker = 1

#def socket_error_handler(exception, socket):


while checker == 1:
    data = input('% ')
    args = data.split()

    try:
        if args[0] == "reset":
            data = "X"
            numtimes = 1
        else:
            data = "X" * int(args[0])
            numtimes = int(args[1])
    except:
        data = None
        numtimes = None
        print("Error, you need to specify two numbers.\n- Number of bytes to send\n- Number of times to send them")

    if not data:
        pass
    else:
        try:
            data_bytes = bytes(data, 'ascii')
            serverudp.send(data.encode())

            for x in range(numtimes):
                if serverudp.send(data.encode()):
                    print("*", end='\n')
                    time.sleep(0.5)

                elif x not in range(numtimes):
                    print(".")
                    # added slight sleep just so i don't overload the socket (.5)
                    time.sleep(0.5)
                    print("Done")

        except OSError as err:
            print("**Connection Error**:\n-Please check the below message-\n%s" % err)
            #print("Send failed!")

            """
                    The maximum payload size of a UDP packet is **65,507** bytes. 
                    To send more than 65507 bytes, I'll need to split the data up across multiple UDP packets
                    (or use TCP instead).
                    
                """

checker = 2
serverudp.close()
