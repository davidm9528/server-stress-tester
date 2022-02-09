from csv import Sniffer
import socket
from socket import *
import time
import threading


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

ip = "127.0.0.1"
port = 1010

#ip.addr ==  127.0.0.1 and tcp.port == 1010
#ip.addr ==  143.117.100.224 and tcp.port == 6011

s = socket(AF_INET, SOCK_STREAM)

#duplicates the socket
#s.dup()

#try:
    #tcp

    #s.settimeout(10)
#except OSError as error1:
    #print("Nope!!\n5%s" % error1 )
    # Connect with above IP and Port

    #s.settimeout(None)

# formatting
startOfCon = time.perf_counter()
s.connect((ip,port))

print("\n")
print("-" * 60)
print("Connection time (seconds): %s" % (time.perf_counter() - startOfCon))
print("client.py")
print("-" * 60)
print("Target: ")
print("Server is running on %s port %s" % (ip, port))
print("-" * 60)
print("Please type which request to send:\nI.e. two 5\nwill send the 2nd request 5 times:\n\n0. req0\n1. req1\n2. req2")
print("-" * 20)

#def socket_error_handler(exception, socket):
while True:
    data = input('\n% ')
    args = data.split()

    try:
        if args[0] == "reset":
            req1 = "X"
            numtimes = 1
        
        elif args[0] == "zero":
            choice = req0
            numtimes = int(args[1])
            
        elif args[0] == "one":
            choice = req1
            numtimes = int(args[1])
        
        elif args[0] == "two":
            choice = req2
            numtimes = int(args[1])
            
        else: #valid option, but not any of the requests selected  (improved error handling, rather than crashing the system)
            print("You have just sent mock text, this is not a valid request.")
            choice = mock 
            numtimes = 1 #Just sends mock once, enter more user validation
    except:
        data = None
        numtimes = None
        print("Error, you need to specify two numbers.\n- Which request to send\n- Number of times to send it")

    if not data:
        pass
    else:
        try:

            for X in range(numtimes):
                   # s.dup()
                    print("*", sep=' ', end=' ', flush=True)
                    
            if s.sendall(choice.encode()):
                    print("test")
                    
            elif X not in range(numtimes):
                    print(".")
                    print("Done")

        except OSError as err:
            print("-Connection Error-:\n-Please check the below message-\n%s" % err)
            #print("Send failed!")

