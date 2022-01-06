from ctypes import addressof
import socket

if __name__ == "__main__":
    ip = "127.0.0.1"
    port = 1234

#IPV4, TCP Connection vvvvv
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Bind ip with port
server.bind((ip,port))

#Listen for 5 Clients (will refuse if 5+ clients try to connect)
server.listen(5)

while True:
    client, address = server.accept()
    print(f"Connection Established - {address[0]}:{address[1]}")

    #1024 # of bytes server will recieve
    string = client.recv(1024)

    string = string.decode("utf-8")
    print(string)

    client.close()