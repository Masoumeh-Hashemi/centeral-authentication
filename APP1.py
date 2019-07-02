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
list_of_session_id=['2019-06-3016:39:50.644369 3']

class app:
    #attributes
    app_code: int 
    app_name: ""
    app_url:url
    # app_secret_code: ""

    #functions
    
    # def __init__(self,Appname):
    #     self.app_name=Appname
        

    def handshake(self,app_name,app_secret_code):
        
        #should return bool ,appcode
        return app.app_code
################################# Register APP ##############################################
    #TODO:register requset for app
    def register_request_to_g(self,appname,url):
        str="register_app "+ appname +" " + url
        result = app_socket.send_request(str,8080)
        return result



################################# Redirect user to G for log in #############################
    #create session id 
    def create_session_id(self):
        #TODO:make sessionId more complicated
        now = datetime.datetime.now()
        session_id=now.__str__()
        session_id = ''.join(session_id.split())
        return str(session_id)

    
    #user requsted for login and app create session id and app code for user to take it to G
    def send_session_id_app_code_to_user(self,inputt):
        app_instance2=app()
        session_id =app_instance2.create_session_id()
        my_query="SELECT app_code FROM app_table WHERE app_name= '"+inputt+"'"
        app_code=db.rert(my_query)
        app_code=(''.join(map(str, app_code.pop())))
        # print(app_code)
        result =session_id + " " + app_code
        # list_of_session_id.append(result)
        # print(list_of_session_id)
        return result

################################## register_user #############################################

    #redirect user for register to G
    def register_user(self,input):
            return "register_user"
################################### retrive user_ids from G ##################################

#user now has sent the session id and app id to G, and App wants to know wich user it was
# first step: send app code and app_secret code to G
#TOFO:make these work
    def request_for_check_app_secret_code(self):
        # if list_of_session_id == []:
        #     print("there is no session id")

        if list_of_session_id != []:
            retreived_session_app_id=list_of_session_id[0]
            #app should send app-secret-code to G before receving user id
            sessionid_appid = retreived_session_app_id.split(' ')
            # print(sessionid_appid[1])
            my_query="SELECT app_secret_code FROM app_table WHERE app_code=='"+sessionid_appid[1]+"' "
            app_secret_code=db.rert(my_query)
            if app_secret_code != []:
                string="app_secret_code "+(''.join(map(str, app_secret_code.pop())))+" "+sessionid_appid[1]
                result1 = app_socket.send_request(string,8080)
                return result1
            if app_secret_code == []:
                print("this app is not registred")

#after checking app_secret code,by above function,now its time to receive user ids
    def request_for_receive_user_id(self):
        app_instance2=app()
        result=app_instance2.request_for_check_app_secret_code()
        if result ==b'True':
            retreived_session_app_id=list_of_session_id.pop()
            # print(retreived_session_app_id)
            last_sessionid_appid="get_user_id"+" "+retreived_session_app_id
            result1 = app_socket.send_request(last_sessionid_appid,8080)
            return result1

        #     # TODO:now app must keep session id + userid(result1) to a cookie
        # elif():
        #     print("This app is not allowed to receive user_ids")

        
################################### pick related events ########################################

    def pick_login_events(self,inputt):
        my_query1="SELECT app_channel_id FROM app_table WHERE app_name=='"+inputt+"' "
        result=db.rert(my_query1)
        if result[0]!=(None,):
            channel_number=(''.join(map(str, result.pop())))
            my_query2 = "SELECT channel_secret FROM esb_table WHERE channel_id=='"+channel_number+"' "
            result2 = db.rert(my_query2)
            channel_secret="request_for_event "+(''.join(map(str, result2.pop())))
            app_socket.send_request(channel_secret,8083)
        if result[0]==(None,):
            print("app has not subscribed to a channel yet!")
            return ""

################################# subcribe to a channel #######################################
    def subcribe_to_channel(self,appname,channelname1):
        my_query1="SELECT app_secret_code FROM app_table WHERE app_name=='"+appname+"' "
        result=db.rert(my_query1)
        if result==[]:
            print("There is not such a app!")
        if result!=[]:
            app_secret_code=(''.join(map(str, result.pop())))
            my_query2 = "SELECT channel_secret FROM esb_table WHERE channel_name=='"+channelname1+"' "
            result2 = db.rert(my_query2)
            #TODO:why str function doesnt work
            channel_secret_code=(''.join(map(str, result2.pop())))
            string_to_send="add_subscriber "+app_secret_code +" "+ channel_secret_code
            print(string_to_send)
            app_socket.send_request(string_to_send,8083)
        

#################################### leave a channel #########################################
    def leave_channel(self,appname):
        my_query1="SELECT app_secret_code FROM app_table WHERE app_name=='"+appname+"' "
        result=db.rert(my_query1)
        app_secret_code=(''.join(map(str, result.pop())))
        string_to_send="unsubscribe "+app_secret_code
        app_socket.send_request(string_to_send,8083)


################################## main operation #############################################

#main operation of the app:just send user a session id and app code
def main_operator(input):
    app_instance=app()
    if input[0] == "login":
        result=app_instance.send_session_id_app_code_to_user(input[1])
        # app_instance.request_for_receive_user_id()
        return result
    if input[0] == "register_user":
        return app_instance.register_user(input[0])

############################################################################################
#a function for listening to network that will be handelled by a thread
def listening():
    app_socket.start_listening(main_operator)
    
app_instance3=app()

    ## register a app to G
# app_instance3.register_request_to_g('automation','automation.com')


    #pick events from esb
# app_instance3.pick_login_events('automation')

    #subscribe to channel
# app_instance3.subcribe_to_channel('maali','first channel')

    #leave channel
# app_instance3.leave_channel("refahi")

    #receive user id by session id from g
# app_instance3.request_for_receive_user_id()


#define 2 threads for listening and do the rest
# thread2 = threading.Thread(target = subcribe_to_channel('automation','first channel'))
# thread2.start()
thread1 = threading.Thread(target = listening(),)
thread1.start()

