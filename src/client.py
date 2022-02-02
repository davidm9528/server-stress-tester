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
ip = "143.117.100.224"
port = 6011

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
print("Please select which request (letter) to send:\na. req0\nb. req1\nc. req2")
print("-" * 20)

#def socket_error_handler(exception, socket):
while True:
    data = input('\n% ')
    args = data.split()

    try:
        if args[0] == "reset":
            req1 = "X"
            numtimes = 1
        else:
            #req0 = req0 * int(args[0])
            req1 = req1 * int(args[0])
            numtimes = int(args[1])
    except:
        mock = None
        numtimes = None
        print("Error, you need to specify two numbers.\n- Which request to send\n- Number of times to send it")

    if not data:
        pass
    else:
        try:
            #data_bytes = bytes(data, 'ascii')
            #s.send(data.encode())
            #s.send(mock.encode())

            for X in range(numtimes):
                if s.send(req1.encode()):
                    print("*", sep=' ', end=' ', flush=True)
                    #time.sleep(0.5)
                    
                    
                    #attempt to recieve response from server
                    #print(reply)
                    response = s.recv(1024)
                    print(response)



                    s.close()
                    
                elif X not in range(numtimes):
                    print(".")
                    print("Done")

        except OSError as err:
            print("-Connection Error-:\n-Please check the below message-\n%s" % err)
            #print("Send failed!")

