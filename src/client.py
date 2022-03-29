
import socket, time, sys, datetime
from socket import *
#import pyshark
import os
#import pycurl

#REQUESTS
file0 = open("txt/davidrequest0.txt")
file1 = open("txt/davidrequest1.txt")
file2 = open("txt/davidrequest2.txt")

filemock = open("txt/mock.txt")

#OPEN REQUESTS
req0 = file0.read().replace("","")
req1 = file1.read().replace("","")
req2 = file2.read().replace("","")

mock = filemock.read().replace("","")

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
client = socket(AF_INET, SOCK_STREAM)

#Formatting
startOfCon = time.perf_counter()

client.connect((ip, port))

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
            
        elif args[0] == "exit":
            client.close()
            
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
        try:
            counter = 0
            s_start = time.perf_counter()
            for X in range(numtimes):
                    counter+=1
                    #client.dup()
                    print("*", sep='', end='', flush=True)
                    
                    if client.sendall(choice.encode()):
                        print("test")

                    elif X not in range(numtimes):
                            print(".")
                            print("Done")
                            
            print("\n")
            s_end = time.perf_counter()
            
            r_start = time.perf_counter()         
            databytes = client.recv(17185)
            r_end = time.perf_counter()

            #buffer needs looked at
            
            '''
            define a function that checks if all the databytes have been received, if not, it will keep trying to receive
            Once it has received all the databytes, it will print the databytes and the time it took to receive them
            '''
            def datarecv(databytes):
                if not databytes:
                    print("No data received")
                else:
                    print("Data received:\n %s" % databytes.decode('utf-8'))
                    
            datarecv(databytes)
            
            if choice != mock:
                
                print("-" * 60)
                '''
                print(".")
                time.sleep(0.5)
                print("..")
                time.sleep(0.5)
                print("...")
                time.sleep(0.5)
                print("-" * 60)
                '''
                reqsize = len(choice)
                
                print("-" * 10 + "Stats" + "-" * 10)
                print(str(counter) + " " + str(args[0]) + " occurance(s) were sent to " + str(ip) + ":" + str(port))    
                #message showing size of request sent
                print("Size of rquest sent to server: " + str((reqsize*numtimes)) + " bytes")  
                print("Size of response from server: "+ str(len(databytes)), "bytes")
                
                send_time = s_end - s_start
                recv_time = r_end - r_start
                avg_time = (send_time + recv_time) / 2
                
                format_send_time = "{:.7f}".format(send_time)
                format_recv_time = "{:.7f}".format(recv_time)
                format_avg_time = "{:.7f}".format(avg_time)
                roundtime = "{:.7f}".format(send_time + recv_time)
                
                print("Time to send %s request(s): %s" % (numtimes, format_send_time) + " seconds")
                print("Time to receive reply: %s" % (format_recv_time) + " seconds")
                print("Roundtime: " + roundtime + " seconds")
                print("Avg: %s" % (float(format_avg_time)) + " seconds")
                print("-" * 60)

        except OSError as err:
            print("-Connection Error-:\n-Please check the below message-\n%s" % err)
            #print("Send failed!")  
                    
    #client.close()