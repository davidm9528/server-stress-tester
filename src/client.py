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

ip = "143.117.100.224"
port = 6011

#try:
    #tcp
s = socket(AF_INET, SOCK_STREAM)
    #s.settimeout(10)
#except OSError as error1:
    #print("Nope!!\n5%s" % error1 )
    # Connect with above IP and Port
s.connect((ip, port))
    #s.settimeout(None)

# formatting
print("\n")
print("-" * 60)
print("client.py")
print("-" * 60)
print("Starting client, press ctrl+c to end.")
print("\nTarget: ")

print("Server is running on %s port %s" % (ip, port))
print("-" * 60)

checker = 1

#def socket_error_handler(exception, socket):

while checker == 1:
    data = input('\n% ')
    args = data.split()

    try:
        if args[0] == "reset":
            req2 = "X"
            numtimes = 1
        else:
            req2 = req2 * int(args[0])
            numtimes = int(args[1])
    except:
        data = None
        numtimes = None
        print("Error, you need to specify two numbers.\n- Which request to send\n- Number of times to send it")

    if not data:
        pass
    else:
        try:
        #    data_bytes = bytes(data, 'ascii')
        #    s.send(data.encode())
            s.send(req2.encode())

            for x in range(numtimes):
                if s.send(req2.encode("ascii", "ignore")):
                    print("*", sep=' ', end=' ', flush=True)
<<<<<<< HEAD
                   # time.sleep(0.5)
=======
                    time.sleep(0.5)
                    
                    #attempt to recieve response from server
                    response = s.recv(1024)
                      
>>>>>>> c2a65f82954789ff0415e102eb6e8b28806114fb

                    #attempt to recieve response from server
                    response = s.recv(1024)
                      
                elif x not in range(numtimes):
                    print(".")
                    print("Done")

        except OSError as err:
            print("**Connection Error**:\n-Please check the below message-\n%s" % err)
            #print("Send failed!")

checker = 2
<<<<<<< HEAD
#s.close()
=======
s.close()

>>>>>>> c2a65f82954789ff0415e102eb6e8b28806114fb
