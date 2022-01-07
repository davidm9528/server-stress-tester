from ctypes import addressof
import socket
import time

#
#CHANGE PORT ON RUNS ON BOTH FILES (CLIENT)
#
if __name__ == "__main__":
    ip = "0.0.0.0"
    port = 4455
    buffer = 102400

#IPV4, TCP, create socket and bind to address
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip,port))

#listen for 5 Clients (will refuse if 5+ clients try to connect)
server.listen(5)

#formatting
print("\n")
print("-" * 60)
print("server.py")
print("-" * 60)
print  ("Starting TCP receive server...  control-break to exit.")
print  ("\nWaiting for data...")
print("-" * 60)

# total bytes recieved since last 'reset'
totalbytes = 0

# -1 is a deliberately invalid timestamp
timestamp = -1

# the total number of bursts that have come in
totalrcvs = 0

while True:
    client, address = server.accept()
    print(f"Connection Established - {address[0]}:{address[1]}")
    
    #Will call this from client.py / not yet implemented
    data, address = server.recvfrom(buffer)

    if not data:
        print("No data entered")
        break
    else:
        finishedstamp = time.time()
        data = len(data)
        totalbytes += data
        totalrcvs += 1

#displayign number of bytes sent kbps
        rate = totalbytes/(finishedstamp - timestamp) * 8 / 1000
        print("\nRcvd: %s bytes, %s total in %s s at %s kbps") % (data, totalbytes, finishedstamp - timestamp, rate)

    #1024 # of bytes server will recieve
    string = client.recv(1024)

    string = string.decode("utf-8")
    print(string)

    client.close()