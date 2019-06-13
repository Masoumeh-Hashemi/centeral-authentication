# Author: @Masoumeh-Hashemi
# Date: June 10 2019
# Description: Handles all network operations

# Importing dependecies
import socket

class layer7:

    # Class variables
    HOST = ''
    PORT = 0

    # Class constructor
    def __init__(self, host, port):
        # TODO: handle socket stuff
        self.HOST = host
        self.PORT = port

    # This will send requests to other servers
    def send_request(self, input,port):
        # TODO: test the following code
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((self.HOST, self.PORT))
        client.send(input)
        from_server = client.recv(4096)
        client.close()
        return from_server

    # This will listen network
    def start_listening(self, function_to_callback):
        # Listen network
        serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serv.bind((self.HOST, self.PORT))
        serv.listen(5)

        # Network stuff
        while True:
            # Accept packets
            conn, addr = serv.accept()
            # Recieve data
            data_ready = ''
            while True:
                data = conn.recv(4096)
                if not data: break
                data_ready += str(data, encoding = "UTF-8")
            # Call operator
            input_array = data_ready.split(' ')
            # Callback trigger
            result = function_to_callback(input_array)
            print (result)
            # Return result to client
            conn.sendall(bytes(result, encoding = "UTF-8"))
            # Close connection
            conn.close()