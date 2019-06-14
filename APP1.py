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
db = DB.db('database.db')
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

def create_session_id():
    #TODO:make sessionId more complicated
    now = datetime.datetime.now()
    session_id=now.__str__()
    session_id = ''.join(session_id.split())
    return session_id

def main_operator(input):
    if input[0] == "login":
        result=[]
        result.append(create_session_id())
        my_query="SELECT app_code FROM app_table WHERE app_name= '"+input[1]+"'"
        app_code=db.rert(my_query)
        print(app_code)
        c=""
        c=app_code[0].__str__()
        result.append(c)
        app_socket.send_request(result,8082)

    elif input[0] == "register":
        # TODO:do what is needed for register
        pass
   
    else:
        return "Command not found"

# app1.handshake("app1","TODO:wait to function register_app")
# app_socket.start_listening(just_print)
# app_socket.send_request(app1.create_session_id(),8080)
app_socket.start_listening(main_operator)
