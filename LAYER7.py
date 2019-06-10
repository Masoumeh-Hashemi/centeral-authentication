import socket

class layer7:

    HOST = ''
    PORT = 0

    def __init__(self, host, port):
        # TODO: handle socket stuff
        self.HOST = host
        self.PORT = port

    def send_request(self, input):
        # TODO: test the following code
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((self.HOST, self.PORT))
        client.send(input)
        from_server = client.recv(4096)
        client.close()
        return from_server

    def start_listening(self, function_to_callback):
        # TODO: callblack story
        a = 1