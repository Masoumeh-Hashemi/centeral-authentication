# Author: @Masoumeh-Hashemi
# Date: June 10 2019
# Description: Handles all network operations

# Importing dependecies
import socket
import DB
import LAYER7
import time
import datetime
from _thread import *
import threading


# Define constrains
host = "127.0.0.1"
port = 8081
url="app1.com"

# Initialize classes
db = DB.db('database.db')
app_socket = LAYER7.layer7(host, port)
list_of_session_id=['2019-06-3014:11:03.181410 301']

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
################################### Register APP ##################################
#TODO:register requset for app
def register_request_to_g(appname,url):
    str="register_app "+ appname +" " + url
    result = app_socket.send_request(str,8080)
    return result



########################################## Redirect user to G for log in ###########################################
#create session id 
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
######################################### retrive user_ids from G ###########################################33

#user now has sent the session id and app id to G, and App wants to know wich user it was
# first step: send app code and app_secret code to G

def request_for_check_app_secret_code():
    retreived_session_app_id=list_of_session_id[0]
    #app should send app-secret-code to G before receving user id
    sessionid_appid = retreived_session_app_id.split(' ')
    my_query="SELECT app_secret_code FROM app_table WHERE app_code=='"+sessionid_appid[1]+"' "
    app_secret_code=db.rert(my_query)
    if app_secret_code != []:
        string="app_secret_code "+(''.join(map(str, app_secret_code.pop())))+" "+sessionid_appid[1]
        result1 = app_socket.send_request(string,8080)
        return result1
    if app_secret_code == []:
        print("this app is not registred")


#after checking app_secret code,by above function,now its time to receive user ids
def request_for_receive_user_id():
    result=request_for_check_app_secret_code()
    if result ==b'True':
        retreived_session_app_id=list_of_session_id.pop()
        print(retreived_session_app_id)
        last_sessionid_appid="get_user_id"+" "+retreived_session_app_id
        result1 = app_socket.send_request(last_sessionid_appid,8080)
        # TODO:now app must keep session id + userid(result1) to a cookie
        return result1
        
    else:
        print("This app is not allowed to receive user_ids")
    


################################## register_user #############################################

#redirect user for register to G
def register_user(input):
        return "register_user"

################################## main operation ###############################################

#main operation of the app:just send user a session id and app code
def main_operator(input):
    if input[0] == "login":
        result=send_session_id_app_code_to_user(input[1])
        request_for_receive_user_id()
        return result
    if input[0] == "register_user":
        return register_user(input[0])

############################################################################################
#a function for listening to network that will be handelled by a thread
def listening():
    app_socket.start_listening(main_operator)
    

## this line register a app to G
# register_request_to_g('automation','automation.com')


##this two line check app secret code in G ##
# request_for_check_app_secret_code()
# request_for_receive_user_id()


#define 2 threads for listening and do the rest
# thread2 = threading.Thread(target = request_for_receive_user_id(),)
# thread2.start()
thread1 = threading.Thread(target = listening(),)
thread1.start()

