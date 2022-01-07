from ctypes import addressof
import socket
import time

if __name__ == "__main__":
    ip = "0.0.0.0"
    port = 3344

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

    #1024 # of bytes server will recieve
    string = client.recv(1024)

    string = string.decode("utf-8")
    print(string)

    client.close()