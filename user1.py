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
    def send_request_to_app(self,url):
        action="login"
        requested_app=url
        list=[]
        list.append(action)
        list.append(" ")
        list.append(requested_app)
        str1 = ''.join(list)
        result = user_socket.send_request(str1,8081)
        result.decode('utf_8')
        return result


    def send_request_to_G(self,input):
        v="register_user "+input
        v=str(v)
        print(v)
        result=user_socket.send_request(v,8080)
        if result=="credential":
            username=input("Please enter username: ")
            password=input("Please enter password: ")
            list=[]
            list.append("enter_credential")
            list.append(" ")
            list.append(username)
            list.append(" ")
            list.append(password)
            str1 = ''.join(list)
            str1=str(list)
            print(str1)
            user_socket.send_request(str1,8080)
        return "request to G worked"


#main operation of app for sending username/password to G 
def main_operation(inputt):
    if inputt[0]=="credential":
        username=input("Please enter username: ")
        password=input("Please enter password: ")
        list=[]
        list.append("enter_credential")
        list.append(" ")
        list.append(username)
        list.append(" ")
        list.append(password)
        str1 = ''.join(list)
        print(str1)
        user_socket.send_request(str1,8080)

#start user program
user_test=user()
sesion_app_id=user_test.send_request_to_app('golestanapp')
sesion_app_id=str(sesion_app_id)
# print(sesion_app_id)

# user_test.receive_G_answer()

g_response=user_test.send_request_to_G(sesion_app_id)
print(g_response)

# user_socket.start_listening(main_operation)   



