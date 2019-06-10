import socket
import os
import subprocess

class App:
    #attributes
    Appcode: int 
    Appname: ""
    Url:""
    Appsecret: ""

    
    def __init__(self,Appname,Url,Appsecret):
        self.Appname=Appname
        self.Url=Url
        self.Appsecret=Appsecret


    def Handshake(self,Appname,Appsecret):
        #should return bool ,appcode
        return App.Appcode

##########################################socket connect###########################
s=socket.socket()
host='127.0.0.1'
port=9998
s.connect((host,port))
s.sendall('app 2 is now sending'.encode())
data = s.recv(1024)
print('Received', repr(data))
s.close()


