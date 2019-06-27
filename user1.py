# Author: @Masoumeh-Hashemi
# Date: June 10 2019
# Description: Handles all network operations

# Importing dependecies
import LAYER7

# Define constrains
host = "127.0.0.1"
port = 8082
# Initialize classes
user_socket = LAYER7.layer7(host, port)

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

    #send a login request to app on app socket and app return a session id and app code
    def send_login_request_to_app(self,url):
        action="login"
        requested_app=url
        str = action + " " + requested_app
        result = user_socket.send_request(str,8081)
        return result
        
    #send register request to App
    def send_register_request_to_app(self):
        action="register_user"
        result = user_socket.send_request(action,8081)
        return result


    # def send_register_request_to_G(self):
    #     v="register_user "
    #     result=user_socket.send_request(v,8080)
    #     #TODO: credential is receveid in b'' format should change it to string
    #     # if result=="True":
    #     if True:
    #         print("if statement worked")
    #         username=input("Please enter username: ")
    #         password=input("Please enter password: ")
    #         print("username and password send to G")
    #         str="enter_credential_for_register_user" + " "+ username + " " + password
    #         user_socket.send_request(str,8080)
    #     return ""


 

#start user program
user_test=user()
sesion_app_id=user_test.send_login_request_to_app('golestanapp')


# user_test.receive_G_answer()
# g_response=user_test.send_register_request_to_app()
# print(g_response)
# print(type(g_response))

# main_operation(g_response)
# user_socket.start_listening(main_operation)   



