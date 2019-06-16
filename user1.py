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

    #send a login request to app on app socket and app return a session id and app code
    def send_request_to_app(self,url):
        action="login"
        requested_app=url
        list=[]
        list.append(action)
        list.append(" ")
        list.append(requested_app)
        str1 = ''.join(list)
        result = app_socket.send_request(str1,8081)
        return result


    def send_request_to_G(self,input):
        v="register_user "+input
        app_socket.send_request(v,8080)


#main operation of app for sending username/password to G 
def main_operation(input):
    if input=="credential":
        username=input("Please enter username: ")
        password=input("Please enter password: ")
        list=[]
        list.append("enter_credential")
        list.append(" ")
        list.append(username)
        list.append(" ")
        list.append(password)
        str1 = ''.join(list)
        app_socket.send_request(str1,8080)

#start user program
user_test=user()
sesion_app_id=user_test.send_request_to_app('golestanapp')
sesion_app_id=str(sesion_app_id)
user_test.send_request_to_G(sesion_app_id)
# user_test.receive_G_answer()


app_socket.start_listening(main_operation)   
        


