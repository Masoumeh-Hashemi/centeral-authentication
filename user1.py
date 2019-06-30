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

######################################login user#######################################
 
    #send a login request to app on app socket and app return a session id and app code
    def send_login_request_to_app(self,url):
        action="login"
        requested_app=url
        str = action + " " + requested_app
        result = user_socket.send_request(str,8081)
        # user_socket.send_request(result,8081)
        return result


  #send session id and app id to G : this function at first send request to app buy this function send_login_request_to_app()
#   and take the result to g, and log in sucessfully
    def send_login_to_g(self,appname):
            test_user1=user()
            sesion_app_id=test_user1.send_login_request_to_app(appname)
            a=sesion_app_id.decode('utf-8')
            str = "loginwithcredential"+" "+ a
            user_socket.send_request(str,8080)

##################################### register user #############################
    #send register request to App
    def send_register_request_to_app(self,url):
        action="register_user"
        requested_app=url
        str = action + " " + requested_app
        result = user_socket.send_request(str,8081)
        return result

     #send session id and app id to G
    def send_register_to_g(self,appname):
            test_user1=user()
            str1=test_user1.send_register_request_to_app(appname)
            a=str1.decode('utf-8')
            user_socket.send_request(a,8080)

  ################################ start #####################################

#start user program
test_user=user()

#this line can register a user successfully to g
# test_user.send_register_to_g('golestanapp')

test_user.send_login_to_g('golestanapp')

# main_operation(g_response)



