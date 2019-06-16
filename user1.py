# Author: @Masoumeh-Hashemi
# Date: June 10 2019
# Description: Handles all network operations

# Importing dependecies
import LAYER7

# Define constrains
host = "127.0.0.1"
port = 8082
# Initialize classes
app_socket = LAYER7.layer7(host, port)

class user:
    user_id=int
    user_password=""
    user_username=""

    # def __init__(self,Username,Password):
    
    #     # self.user_username=Username
    #     # self.user_password=Password

    def Login(self):
        pass
        # return user.user_id

    def send_request_to_app(self,url):
        action="login"
        requested_app=url
        list=[]
        list.append(action)
        list.append(" ")
        list.append(requested_app)
        str1 = ''.join(list)
        result = app_socket.send_request(str1,8081)
        # print(result)
        return result
    def send_request_to_G(self,input):
        v="register_user "+input
        app_socket.send_request(v,8080)

        # username=input("Please enter username: ")
        # password=input("Please enter password: ")
        # list=[]
        # list.append(username)
        # list.append(password)
        # return list

#start user program
user_test=user()
a=user_test.send_request_to_app('golestanapp')
a=str(a)
# print(a)
user_test.send_request_to_G(a)

# print(c)
# app_socket.send_request(usertest.send_login_request_to_app(),8081)
# app_socket.start_listening("just_print")   
        


