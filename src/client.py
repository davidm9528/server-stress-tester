import socket, time, sys, datetime
from socket import *
import os
#import networkx as nx
#import matplotlib.pyplot as plt
from socket import AF_INET, SOCK_STREAM

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
ip = "143.117.100.224"
port = 6011

#Queens server
#Wireshark filter
#ip.addr ==  143.117.100.224 and tcp.port == 6011


#Create the client socket
#client = socket(AF_INET, SOCK_STREAM)

startOfCon = time.perf_counter()
#client.connect((ip, port))
endOfCon = time.perf_counter()

def create_sockets(ip,port,num_sockets):
    '''create multiple client sockets'''
    import socket
    sockets = []
    for i in range(int(num_sockets)):
        client = socket.socket(AF_INET, SOCK_STREAM)
        client.connect((ip, port))
        sockets.append(client)
    return sockets

'''
Using NetworkX library, show a graph of the network traffic on the sockets being used

def graphsock():
    G = nx.DiGraph()
    G.add_edge(client.getsockname(), client.getpeername())
    nx.draw_networkx(G, with_labels=True)
    plt.show()
'''          
def main():
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

    while True:
        choice = input('\n% ')
        args = choice.split()
        
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
                close()
                
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
                        
                        print("How many clients would you like to create? ")
                        num_sockets = input("% ")
                        socks = create_sockets(ip, port, num_sockets)
                        num_sockets = int(num_sockets)
                        
                        '''create for loop iterating through all the sockets'''
                        for i in range(num_sockets):
                            socks[i].send(choice.encode())
                        #socks[i].close()
                        #socks = create_sockets(ip, port, num_sockets)
                        
                        '''
                        if socks.send(choice.encode()):
                            print("test")

                        elif X not in range(numtimes):
                                print(".")
                                print("Done")
                        '''        
                print("\n")
                s_end = time.perf_counter()
                
                
                if choice != mock:

                    r_start = time.perf_counter()         
                #databytes = client.recv(8820) 
                
                '''have each client recv the data from the server'''
                for i in range(num_sockets+1):
                    databytes = socks[i-1].recv(8820)
                    databytes2 = socks[i-1].recv(8820)
                    
                    #print(databytes.decode())
                    #uncomment for qub server vvvv
                    #databytes2 = client.recv(8820)      
                    r_end = time.perf_counter()
                
                    #print(databytes2.decode('utf-8'))
                    print(databytes.decode('utf-8') + databytes2.decode('utf-8'))
                    
                print("-" * 60)
                print(".")
                time.sleep(0.5)
                print("..")
                time.sleep(0.5)
                print("...")
                time.sleep(0.5)
                    
                reqsize = len(choice)
                
                print("-" * 15 + "Stats" + "-" * 15)
                print(str(counter) + " " + str(args[0]) + " occurance(s) were sent to " + str(ip) + ":" + str(port))    
                print("Size of rquest sent to server: " + str((reqsize*numtimes)) + " bytes")  
                print("Size of response from server: "+ str(len(databytes2)), "bytes")
                
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
                #graphsock()
                print("-" * 60)
            
            except OSError as err:
                print("-Connection Error-:\n-Please check the below message-\n%s" % err)  
                        
        #client.close()
        
        
        
'''Create a loop iterating through the list of sockets, and then append them to the send function'''
def looper():
      print()  
        
        
if __name__ == "__main__":
    main()