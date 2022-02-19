
import socket, time, sys
from socket import *
import threading

#REQUESTS
file0 = open("txt/davidrequest0.txt")
file1 = open("txt/davidrequest1.txt")
file2 = open("txt/davidrequest2.txt")
filemock = open("txt/mock.txt")

#OPEN REQUESTS
req0 = file0.read().replace("\n"," ")
req1 = file1.read().replace("\n"," ")
req2 = file2.read().replace("\n"," ")
mock = filemock.read().replace("\n"," ")

#CLOSE REQUESTS
file0.close()
file1.close()
file2.close()
filemock.close()

#Localhost server for testing (server.py)
#Wireshark filter
#ip.addr ==  127.0.0.1 and tcp.port == 1010
ip = "127.0.0.1"
port = 1010

#Queens server
#Wireshark filter
#ip.addr ==  143.117.100.224 and tcp.port == 6011

#Create the socket
s = socket(AF_INET, SOCK_STREAM)

sys.setrecursionlimit(2000)

def open_socket(counter):
    sockets = []
    for i in range(counter):
        se = socket(AF_INET, SOCK_STREAM)
        se.bind((ip, port))
        se.listen(1)
        sockets.append(se)
 
    time.sleep(1)

#Formatting
startOfCon = time.perf_counter()

s.connect((ip, port))

 #change buffer size eventually (make it dynamic)

print("\n")
print("-" * 60)
print("Connection time (seconds): %s" % (time.perf_counter() - startOfCon))
print("client.py")
print("-" * 60)
print("Target: ")
print("Server is running on %s port %s" % (ip, port))
print("-" * 60)
print("Please type which request to send:\nI.e. req1 5\nwill send the 1st request 5 times:\n\n- req0 #\n- req1 #\n- req2 #")
print("- reset - clears stats")
print("-" * 20)

#def socket_error_handler(exception, socket):
while True:
    choice = input('\n% ')
    args = choice.split()
    #msg = s.recv(1024)
    try:
        if args[0] == "reset":
            choice = "X"
            numtimes = 1
        
        elif args[0] == "req0":
            choice = req0
            numtimes = int(args[1])
            
            
        elif args[0] == "req1":
            choice = req1
            numtimes = int(args[1])
        
        elif args[0] == "req2":
            choice = req2
            numtimes = int(args[1])
            
        else: #valid option, but not any of the requests selected  (improved error handling, rather than crashing the system)
            print("You have just sent one byte, this is not a valid request.")
            choice = mock 
            numtimes = 1 #Just sends mock once, enter more user validation
    except:
        choice = None
        numtimes = None
        print("Error, you need to specify two correct inputs.\n- Which request to send\n- Number of times to send it")

    if not choice:
        pass
    else:
        
       # socks = open_socket(1)
        
        try:

            for X in range(numtimes):
                    s.dup()
                    print("*", sep=' ', end=' ', flush=True)
                    if s.sendall(choice.encode()):
                            print("test")

                    elif X not in range(numtimes):
                            print(".")
                            print("Done")

        except OSError as err:
            print("-Connection Error-:\n-Please check the below message-\n%s" % err)
            #print("Send failed!")

