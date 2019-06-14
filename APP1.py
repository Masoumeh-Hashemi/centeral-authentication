# Author: @Masoumeh-Hashemi
# Date: June 10 2019
# Description: Handles all network operations

# Importing dependecies
import socket
import DB
import LAYER7
import time
#TODO:how to import these two whrandom,md5
# import whrandom
# import md5
import datetime


# Define constrains
host = "127.0.0.1"
port = 8081

# Initialize classes
app_socket = LAYER7.layer7(host, port)


class app:
    #attributes
    app_code: int 
    app_name: ""
    app_url:""
    app_secret_code: ""

    #functions
    
    def __init__(self,Appname):
        self.app_name=Appname
        

    def handshake(self,app_name,app_secret_code):
        
        #should return bool ,appcode
        return app.app_code

    def create_session_id(self):
        #TODO:make sessionId more complicated
        now = datetime.datetime.now()
        sentence=now.__str__()
        sentence = ''.join(sentence.split())
        return sentence

        #TODO:"""Build a new Session ID"""
        # def getNewSID(self,tag):
            # t1 = time.time()
            # time.sleep( whrandom.random() )
            # t2 = time.time()
            # base = md5.new( tag + str(t1 +t2) )
            # sid = tag + '_' + base.hexdigest()
            # return sid



	

app1=app("golestan")
result=app1.create_session_id()
print (result)
# app1=app("app1")
# app1.handshake("app1","TODO:wait to function register_app")

def just_print(input):
    if input[0]=="app1":
     return "Im working"
# app_socket.start_listening(just_print)
app_socket.send_request(app1.create_session_id(),8080)
