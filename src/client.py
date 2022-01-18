from csv import Sniffer
import socket
from socket import *
import string
import time
#import pyshark
#import pings

file0 = open("txt/davidrequest0.txt")
file1 = open("txt/davidrequest1.txt")
file2 = open("txt/davidrequest2.txt")

req0 = file0.read().replace("\n"," ")
req1 = file1.read().replace("\n"," ")
req2 = file2.read().replace("\n"," ")

file0.close()
file1.close()
file2.close()

#print(req0)

ip = "127.0.0.1"
port = 1010

#tcp
s = socket(AF_INET, SOCK_STREAM)

# Connect with above IP and Port
s.connect((ip, port))

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
    data = input('\n% ')
    args = data.split()

    try:
        if args[0] == "reset":
            req0 = "X"
            numtimes = 1
        else:
            req0 = req0 * int(args[0])
            numtimes = int(args[1])
    except:
        data = None
        numtimes = None
        print("Error, you need to specify two numbers.\n- Number of bytes to send\n- Number of times to send them")

    if not data:
        pass
    else:
        try:
        #    data_bytes = bytes(data, 'ascii')
        #    s.send(data.encode())
            
            s.send(req0.encode())

            for x in range(numtimes):
                if s.send(req0.encode()):
                    print("*", sep=' ', end=' ', flush=True)
                    time.sleep(0.5)
                      

                elif x not in range(numtimes):
                    print(".")
                    # added slight sleep just so i don't overload the socket (.5)
                    #time.sleep(0.5)
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
s.close()
