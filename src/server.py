from socket import *
import socket
import time
from datetime import datetime

#
#CHANGE PORT ON RUNS ON BOTH FILES (CLIENT)
#

ip = "localhost"
port = 1010
buffer = 102400

#create socket and bind to address
serverudp = socket.socket(AF_INET,SOCK_DGRAM)
serverudp.bind((ip,port))

#listen for 1 Clients (will refuse if 1+ clients try to connect)
#serverudp.listen(1)

#formatting
time.time()
print("\n")
print("-" * 60)
print("server.py")
print("-" * 60)
print  ("Starting UDP receive server...  control-break to exit.")
print  ("\nWaiting for data (client.py)...")
print("-" * 60)


# total bytes recieved since last 'reset'
totalbytes = 0
# -1 is a deliberately invalid timestamp
timestamp = -1
# the total number of bursts that have come in
totalrcvs = 0

data, address = serverudp.recvfrom(buffer)

information = socket.getaddrinfo(ip, port, family=AF_INET, proto=AF_INET)

print("-Connection Established-")
dateTimeObj = datetime.now()
timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")
print("Current Timestamp : ", timestampStr)
print("Server Info: ", information)
print("-" * 60)
while (1):
    
    #will call this from client.py / not yet implemented (hehe)
    data, address = serverudp.recvfrom(buffer)
    #print(f"Connection Established - {address[0]}:{address[1]}")

    if not data:
        print("No data entered")
        break
    else:
        
        finishedstamp = time.time()
        
        data = len(data)
        totalbytes += data
        totalrcvs += 1

        #displaying number of bytes sent kbps
        # * 8 /1000 for 8 bits in a byte
        rate = totalbytes/(finishedstamp - timestamp) * 8 / 1000

        print("Rcvd: %s bytes, %s total in %ss at %skbps" % (data, totalbytes, finishedstamp - timestamp, rate))

        #Send 1 single byte to clear stats
        #reset
        if data == True:
            totalbytes = 0
            timestamp = time.time()
            totalrcvs = 0
            print("*Reset* - clearing stats.")
serverudp.close()