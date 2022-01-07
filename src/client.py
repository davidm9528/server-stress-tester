import socket
import string
import time

if __name__ == "__main__":
    ip = "127.0.0.1"
    port = 9988

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    #Connect with above IP and Port
    server.connect((ip,port))

    #formatting
    print("\n")
    print("-" * 60)
    print("client.py")
    print("-" * 60)
    print  ("Starting client, press ctrl+c to end.")
    print  ("\nTarget: ")
    print  ("server.py running on %s port %s" % (ip, port))
    print("-" * 60)

    while (True):
        data = input('% ')
        args = data.split()

        try: 
                if args[0] == "reset":
                    data = "X"
                    numtimes = 1
                else:
                    data = "X" * int(args[0])
                    numtimes = int(args[1])
        except:
                data = None
                numtimes = None
                print("Error, you need to specify two numbers.\n- Number of bytes to send\n- Number of times to send them")

        if not data: 
            pass
        else:
                try:
                    server.send(bytes("X", (ip, port)))

                    for x in range(numtimes):
                        if(server.send(data,(ip,port))):
                            print("*")
                        else:
                            print(".")

                            #added slight sleep just so i dont overload the socket
                            time.sleep(0.1)
                            print("Finished")
                            server.close()
                except:
                    print("Send failed!")
                    server.close()