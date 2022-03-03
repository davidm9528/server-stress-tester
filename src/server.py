from random import choice
from socket import *
import socket
import threading
import time
from datetime import datetime

#
#CHANGE PORT ON RUNS ON BOTH FILES (CLIENT)
#

ip = "127.0.0.1"
port = 1010
buffer = 102400

#create socket and bind to address
#tcp 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((ip,port))

#listen for 1 Clients (will refuse if 1+ clients try to connect)
s.listen(5)

conn, address = s.accept()

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

    data, address = conn.recvfrom(buffer)

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
        conn.send(bytes(str(choice), encoding="utf8"))
        #works ^
        
        #Send 1 single byte to clear stats
        #reset
        if data == True:
            totalbytes = 0
            timestamp = time.time()
            totalrcvs = 0
            print("*Reset* - clearing stats.")
#s.close()