from inspect import trace
import socket
import unittest
import tracemalloc

class client_test(unittest.TestCase):

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('143.117.100.224', 6011))

    def testsend(self):
        self.client_socket.send("req0".encode())
        self.client_socket.close()

    def testrecv(self):
        filereply = open("txt/reply.txt")
        reply = filereply.read().replace("","")
        filereply.close()
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(('143.117.100.224', 6011))
        try:
            self.client_socket.settimeout(1.5)
            self.client_socket.send("req0".encode())
            self.client_socket.recv(8820).decode(), reply 
            self.client_socket.close()
        except:
            print("timeout")

    def testcreate_sockets(self):
        tracemalloc.start()
        sockets = []
        for i in range(5):
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.settimeout(10)
            self.client_socket.connect(('143.117.100.224', 6011))
            self.client_socket.settimeout(None)
            sockets.append(self.client_socket)
        print("Number of sockets: ",len(sockets))


    def client_test(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(('143.117.100.224', 6011))
        self.client_socket.send("req0 1".encode())
        self.assertEqual(self.client_socket.recv(1024).decode(), "req0 1")
        self.client_socket.close()
        print("client tested!!")

    
    '''
    From client.py, check user input is valid (choice == req0, req1, req2)
    '''
    def test_user_input(self):
        print("req0, req1 or req2")
        choice = input('\n% ')
        args = choice.split()
        
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(('143.117.100.224', 6011))
        try:
            self.assertEqual(choice, "req0")
            self.assertEqual(choice, "req1")
            self.assertEqual(choice, "req2")
        except:
            print("Invalid input")
            self.client_socket.close()
    


    def tearDown(self):
        self.client_socket.close()

if __name__ == '__main__':
    unittest.main()
        