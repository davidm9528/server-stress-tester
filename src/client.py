import socket

if __name__ == "__main__":
    ip = "127.0.0.1"
    port = 4455

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    #Connect with above IP and Port
    server.connect((ip,port))


    #sending to server
    string = input("Enter string to send: ")
    server.send(bytes(string, "utf-8"))