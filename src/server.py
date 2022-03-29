from random import choice
from socket import *
import socket
import threading
import time
from datetime import datetime
from time import perf_counter_ns

ip = "127.0.0.1"
port = 1010
buffer = 10000

#
#CHANGE PORT ON RUNS ON BOTH FILES (CLIENT)
#
def main():
    print("Server running, waiting for connection(s)...")
    print(ip + ":" + str(port))

    filereply = open("txt/reply.txt")
    reply = filereply.read().replace("","")
    filereply.close()

    #create socket and bind to address
    #tcp 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.bind((ip,port))

    s.listen(0)

    conn, address = s.accept()
    '''
    def graphsock():
        G = nx.DiGraph()
        G.add_edge(s.getsockname(), s.getpeername())
        nx.draw_networkx(G, with_labels=True)
        plt.show()
    '''
    #formatting
    time.time()
    print("\n")
    print("-" * 60)
    print("server.py")
    print("-" * 60)
    print  ("Starting TCP receive server...  control-break to exit.")
    print  ("\nWaiting for data (client.py)...")
    print("-" * 60)

    # total bytes recieved since last 'reset'
    totalbytes = 0
    # -1 is a deliberately invalid timestamp
    timestamp = -1
    # the total number of bursts that have come in
    totalrcvs = 0

    information = socket.getaddrinfo(ip, port, family=AF_INET, proto=AF_INET)

    print("-Connection Established-")
    dateTimeObj = datetime.now()
    timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")
    print("Current Timestamp : ", timestampStr)
    print("Server Info: ", information)
    print("-" * 60)

    while (1):
        recvs = time.perf_counter_ns()
        data, address = conn.recvfrom(buffer)
        recvf = time.perf_counter_ns()

        if not data:
            print("***Receiving no more data***")
            print("Closing...")
            break
        else:   
            finishedstamp = recvf - recvs
            
            data = len(data)
            totalbytes += data
            totalrcvs += 1

            print("Rcvd: %s bytes, %s total in %sns" % (data, totalbytes, (finishedstamp/1000) - timestamp))
            #graphsock()

            conn.send(bytes(reply, encoding="utf8"))

            #Send 1 single byte to clear stats
            #reset
            if data == True:
                totalbytes = 0
                timestamp = time.perf_counter()
                totalrcvs = 0
                print("*Reset* - clearing stats.")
#s.close()

if __name__ == "__main__":
    main()