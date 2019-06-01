#!/usr/bin/env python3
import socket
import sys
import threading
import time
from queue import Queue


all_connections=[]
all_address=[]

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
    
#binding the socket and listening for connections

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


#andeling connections from multiple clients and saving to a list
#closing previous connections when server is restarted

def accepting_connections():
    for c in all_connections:
        c.close()
    del all_connections[:]
    del all_address[:]
    while True:
        try:
            conn,address=s.accept()
            s.setblocking(1)
            all_connections.append(conn)
            all_address.append(address)
            # ip, port = str(all_address[0]), str(all_address[1])
            print("connection has been stablished :"+ address[0])
        except:
            print("error accepting connections")


#display all current active connections with client
def list_connections():
    # result=''
    for i,conn in enumerate(all_connections):
        try:
            conn.send(str.encode(' '))
            conn.recv(201460)
        except:
            del all_connections[i]
            del all_address[i]
            continue
    # result = (str(i)+"    "+str(all_address[i][0])+"     "+str(all_address[i][1])+"\n")
    # print(result)

def main():
    create_socket()
    bind_socket()
    accepting_connections()
    list_connections()
main()
