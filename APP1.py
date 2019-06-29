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
url="app1.com"

# Initialize classes
db = DB.db('database.db')
app_socket = LAYER7.layer7(host, port)
list_of_session_id=[]

class app:
    #attributes
    app_code: int 
    app_name: ""
    app_url:url
    # app_secret_code: ""

    #functions
    
    def __init__(self,Appname):
        self.app_name=Appname
        

    def handshake(self,app_name,app_secret_code):
        
        #should return bool ,appcode
        return app.app_code


#
def create_session_id():
    #TODO:make sessionId more complicated
    now = datetime.datetime.now()
    session_id=now.__str__()
    session_id = ''.join(session_id.split())
    return str(session_id)

    
#user requsted for login and app create session id and app code for user to take it to G
def send_session_id_app_code_to_user(inputt):
    session_id = create_session_id()
    my_query="SELECT app_code FROM app_table WHERE app_name= '"+inputt+"'"
    app_code=db.rert(my_query)
    app_code=(''.join(map(str, app_code.pop())))
    result =session_id + " " + app_code
    list_of_session_id.append(result)
    # print(list_of_session_id)
    
    return result

def request_for_receive_user_id():
    result=list_of_session_id.pop()
    print(result)
    list_of_session_id1=(''.join(map(str, result)))
    last_sessionid_appid="getuserid"+" "+list_of_session_id1
    print(last_sessionid_appid)
    app_socket.send_request(last_sessionid_appid,8080)

#main operation of the app:just send user a session id and app code
def main_operator(input):
    if input[0] == "login":
        return send_session_id_app_code_to_user(input[1])
    if input[0] == "register_user":
        #TODO:register part
        pass

app_socket.start_listening(main_operator)
request_for_receive_user_id()
