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
filemock = open("txt/mocktext.txt")

req0 = file0.read().replace("\n"," ")
req1 = file1.read().replace("\n"," ")
req2 = file2.read().replace("\n"," ")
mock = filemock.read().replace("\n"," ")

file0.close()
file1.close()
file2.close()
filemock.close()

#print(req0)

#ip = "143.117.100.224"
#port = 6011
ip = "127.0.0.1"
port = 1010

s = socket(AF_INET, SOCK_STREAM)
s.connect((ip, port))

#duplicates the socket
s.dup()

#try:
    #tcp

    #s.settimeout(10)
#except OSError as error1:
    #print("Nope!!\n5%s" % error1 )
    # Connect with above IP and Port

    #s.settimeout(None)

# formatting
print("\n")
print("-" * 60)
print("client.py")
print("-" * 60)
print("Target: ")
print("Server is running on %s port %s" % (ip, port))
print("-" * 60)
print("Please select which request (number) to send:\n0. req0\n1. req1\n2. req2")
print("-" * 20)

#def socket_error_handler(exception, socket):
while True:
    data = input('\n% ')
    args = data.split()

    try:
        if args[0] == "reset":
            req0 = "X"
            numtimes = 1
        
        elif args[0] == "zero":
            choice = req0
            numtimes = int(args[1])
        else: #valid option, but not any of the requests selected
            choice = mock 
            numtimes = 1
    except:
        mock = None
        numtimes = None
        print("Error, you need to specify two numbers.\n- Which request to send\n- Number of times to send it")

    if not data:
        pass
    else:
        try:

            for X in range(numtimes):
                if s.sendall(req0.encode()):
                    print("test")
                    print("*", sep=' ', end=' ', flush=True)

                elif X not in range(numtimes):
                    print(".")
                    print("Done")

        except OSError as err:
            print("-Connection Error-:\n-Please check the below message-\n%s" % err)
            #print("Send failed!")

s.close()