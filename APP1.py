# Author: @Masoumeh-Hashemi
# Date: June 10 2019
# Description: Handles all network operations

# Importing dependecies
import socket
import DB
import LAYER7

# Define constrains

host = "127.0.0.1"
port = 8080

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
        # TODO:sessionid
        pass


# app1=app("app1")
# app1.handshake("app1","TODO:wait to function register_app")
#"TODO:listening network ready to call any function instead of main_operator"

# app_socket.send_request("TODO:sending what we want to server",8080)
def just_print(input):
    if input[0]=="app1":
     return print("Im working")
app_socket.start_listening(just_print)