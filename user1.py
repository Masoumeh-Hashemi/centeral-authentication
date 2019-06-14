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

    def send_login_request_to_app(self):
        action="login"
        requested_app=input("Please enter app name: ")
        list=[]
        list.append(action)
        list.append(" ")
        list.append(requested_app)
        c=""
        c=str(list)
        app_socket.send_request(c,8081)

        # username=input("Please enter username: ")
        # password=input("Please enter password: ")
        # list=[]
        # list.append(username)
        # list.append(password)
        # return list
      


usertest=user()
# c=usertest.send_login_request_to_app()

# print(c)
        
app_socket.send_request(usertest.send_login_request_to_app(),8081)
# app_socket.start_listening("just_print")   
        


