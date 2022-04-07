import time
from socket import *
#import networkx as nx
import matplotlib.pyplot as plt
from socket import AF_INET, SOCK_STREAM
from scipy.stats import linregress
import numpy as np

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

startOfRun = time.perf_counter()
#client.connect((ip, port))
endOfRun = time.perf_counter()

runProg = endOfRun - startOfRun

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
    print("Connection time (seconds): %s" % (time.perf_counter() - runProg))
    print("client.py")
    print("-" * 60)
    print("Target: ")
    print("Server is running on %s port %s" % (ip, port))
    print("-" * 60)
    print("Please type which request to send:\nI.e. req1 5\nwill send the 1st request 5 times:\n\n- req0 #\n- req1 #\n- req2 #")
    print("- reset - clears stats")
    print("-" * 20)
    list_of_s_lists = []
    avgl = []
    flag = 1
    while flag == 1:
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
            '''    
            else: #valid option, but not any of the requests selected  (improved error handling, rather than crashing the system)
                print("You have just sent one byte, this is not a valid request.")
                choice = mock 
                numtimes = 1 #Just sends mock once, enter more user validation
            '''
        except:
            choice = None
            numtimes = None
            print("Error, you need to specify two correct inputs.\n- Which request to send\n- Number of times to send it")

        if not choice:
            pass
        else:
            try:
                list_avgs = []
                counter = 0
                s_start = time.perf_counter()
                for X in range(numtimes):
                        counter+=1
                        print("How many clients would you like to create? ")
                        num_sockets = input("% ")
                        socks = create_sockets(ip, port, num_sockets)
                        num_sockets = int(num_sockets)
                        
                        '''create for loop iterating through all the sockets'''
                        for i in range(num_sockets):
                            socks[i].send(choice.encode())
                s_end = time.perf_counter()              
                print("\n")
                
                send_time = s_end - s_start
                format_send_time = "{:.7f}".format(send_time)
                
                if choice != mock:
                    r_start = time.perf_counter()          
                
                '''have each client recv the data from the server'''
                for i in range(num_sockets):
                    databytes = socks[i-1].recv(8820)
                    databytes2 = socks[i-1].recv(8820)
     
                    r_end = time.perf_counter()
                    recv_time = r_end - r_start

                    format_recv_time = "{:.7f}".format(recv_time)

                    avg_time = (send_time + recv_time) / 2
                    format_avg_time = "{:.7f}".format(avg_time)   
                    roundtime = "{:.7f}".format(send_time + recv_time)

                    #print(databytes.decode('utf-8') + databytes2.decode('utf-8'))
                    list_avgs.append(format_avg_time)
                    
                    '''total the elements of avg_time_l, divide by num_sockets'''
                    meanavg = sum(float(i) for i in list_avgs) / num_sockets
                    format_meanavg = "{:.7f}".format(float(meanavg))
    
                print("-" * 60)
                print(".")
                time.sleep(0.25)
                print("..")
                time.sleep(0.25)
                print("...")
                time.sleep(0.25)
                    
                reqsize = len(choice)
                
                print("-" * 15 + "Stats" + "-" * 15)
                print(str(counter) + " " + str(args[0]) + " occurance(s) were sent to " + str(ip) + ":" + str(port))    
                print("Size of rquest sent to server: " + str((reqsize*numtimes)) + " bytes")  
                print("Size of response from server: "+ str(len(databytes2)), "bytes")

                print("Time to send %s request(s): %s" % (numtimes, format_send_time) + " seconds")
                print("Time to receive reply: %s" % (format_recv_time) + " seconds")
                print("Roundtime: " + roundtime + " seconds")
                print("Avg: %s" % (float(format_meanavg)) + " seconds")
                
                print("-" * 60)
                print(".")
                time.sleep(0.25)
                print("..")
                time.sleep(0.25)
                print("...")
                time.sleep(0.25)

                sockets_l = [i for i in range(1, num_sockets+1)]
            
                print("\nWould you like to send more data? (y/Y or n/N)")
                print("-" * 60)
                decision = input(":")
                print("-" * 60)

                if decision == "y" or decision == "Y":
                    print("Please type which request to send:\nI.e. req1 5\nwill send the 1st request 5 times:\n\n- req0 #\n- req1 #\n- req2 #")
                    print("-" * 60)
                    list_of_s_lists.append(len(sockets_l))
                    avgl.append(meanavg)
                    flag = 1 #keeps the loop going
                    print(decision)   
                elif decision == "n" or decision == "N": 
                    list_of_s_lists.append(len(sockets_l))
                    avgl.append(meanavg)
                    flag = 0 #ends the loop   
                    print(decision)  
                else:
                    decision != "y" or decision != "Y" or decision != "n" or decision != "N"
                    flag = 0
                    print("**Please enter a valid option**")

            except OSError as err:
                print("**Connection Error**\n**Please check the below message**\n%s" % err)  

    #print(list_avgs)
    #print(meanavg)

    print(avgl)
    print(list_of_s_lists)
    values = range(len(list_of_s_lists))

    slope, intercept, r_value, p_value, std_err = linregress(values, avgl)
    print("slope: %f, intercept: %f" % (slope, intercept))
    print("R-squared: %f" % r_value**2)
    plt.title('Client send and receive average time')
    plt.xlabel('Number of clients (sending 1 request each)')
    plt.ylabel('Average Time (seconds)')
    
    plt.plot(values, avgl, marker='o', linestyle='--', color='b')
    plt.plot(values, intercept + slope*values, 'r', label='fitted line')
    plt.xticks(values, list_of_s_lists)

    #plt.style.use('ggplot')
    #plt.xticks(np.arange(len(list_of_s_lists), num_sockets+1, 1))
    #plt.bar((list_of_s_lists), avgl, color='red')
    #plt.yticks(np.arange((0.00*0.01), 3.5, 0.5))

    plt.show()

if __name__ == "__main__":
    main()