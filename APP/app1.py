import socket
import os
import subprocess
import random
import string
import datetime

import CORE.layer7

class App():
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

########################################## sending data to server socket ###########################
def send(str):
    data_to_send=str
    s=socket.socket()
    host='127.0.0.1'
    port=9998
    s.connect((host,port))
    s.send(data_to_send.encode())
    data = s.recv(1024)
    print('Received', repr(data))
    s.close()
################################################ using send function ################################
# test_data='Im app 1 in variable'
# send('Im testing')
############################################ generate session id #####################################
#generate random string
def random_string_generator(stringLength=10):
    """Generate a random string of letters, digits and special characters """

    password_characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(password_characters) for i in range(stringLength))

#get current date and time
def get_time():
   current_dt = datetime.datetime.now()
   return current_dt

#generate session (random string+date and time)
def generate_session_id():
    var1=random_string_generator()
    var2=get_time()
    session_id=var1+str(var2)
    return session_id

###################################################################################################

val1=generate_session_id()
print(val1)
