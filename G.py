# Author: @Masoumeh-Hashemi
# Date: June 10 2019
# Description: Handles all network operations

# Importing dependecies
import uuid
import socket
import DB
import LAYER7


# Define constrains
dbname = 'database.db'
host = "127.0.0.1"
port = 8080

# Initialize classes
db = DB.db(dbname)
sockett = LAYER7.layer7(host, port)

# Application functionality
def main_operator(input):
    if input[0] == "register_user":
        return register_user()

    elif input[0] == "register_app":
        c= register_app(input[1], input[2])
        return c

    #user has sessionid + appid from app and wants to login
    elif input[0] == "login_with_credential":
        return login_with_credential(input[1],input[2])
   
    elif input[0] == "get_user_id":
        return return_logged_user_id_to_app(input[1],input[2])

    elif input[0] == "app_secret_code":
        return check_app_secret_code(input[1],input[2])
        
    else:
        print("command not found")
############################################## User##################################################

# LOGIN USER
#user has session id and app code and wants to login
#code working well
def login_with_credential(sessionid,appid):
        username=input("Please enter username: ")
        password=input("Please enter password: ")
        get_userid_query="SELECT user_id FROM user_table WHERE user_username= '"+username+"' AND user_password= '"+password+"'"
        result=db.rert(get_userid_query)
        if result == []:
            print("wrong username or password")
            return login_with_credential(sessionid,appid)
        elif result!= []:
            user_id=(''.join(map(str, result.pop())))
            print(user_id)
            print("user successfully loged in")
            add_to_sessiontable_query="INSERT INTO session_table(session_id,s_app_id,s_user_id) VALUES ('"+sessionid+"','"+appid+"','"+user_id+"')"
            db.execute(add_to_sessiontable_query)
            ################### send event to esb######################
            my_query="SELECT app_channel_id FROM app_table WHERE app_code= '"+appid+"' "
            channel_id_lists = db.rert(my_query)
            channel_id=channel_id_lists[0]
            channel_id=(''.join(map(str, channel_id)))
            str1 = "login_event " + appid +" "+ user_id + " " + channel_id
            print(str1)
            sockett.send_request(str1,8083)
            return ""

        
#REGISTER USER
# regsiter function,at first it receives an session_id and app_id from requsted user and ask for credentials
def register_user():
    print("register_user worked")
    username=input("Please enter username: ")
    password=input("Please enter password: ")
    my_query = "INSERT INTO user_table( user_username,user_password) VALUES ('"+username+"','"+password+"')"
    db.execute(my_query)
    print( "You are going to register " + username + " with pass: " + password )
    # return result
    return "new user added"


################################################ App ##################################################
#create random string for app_secret_code
def generate_random_string():
    stringLength = 8
    randomString = uuid.uuid4().hex # get a random string in a UUID fromat
    randomString  = randomString.upper()[0:stringLength] # convert it in a uppercase letter and trim to your size.
    return str(randomString)

    
#register App function and return secret_app_code to the app who called it   
def register_app(appname, url):
    a=appname
    b=url
    c=generate_random_string()
    my_query = "INSERT INTO app_table(app_secret_code,app_name,app_url) VALUES ('"+c+"','"+a+"','"+b+"')"
    db.execute(my_query)
    print("App " + a + " registered with URL: " + b)   
    return c
########################################## check app secret code #############################################

#app send its app_code and app_secret_code and G check if they are synche
def check_app_secret_code(app_secret_code,app_code):
    my_query="SELECT app_secret_code FROM app_table WHERE app_code ='"+app_code+"' "
    result=db.rert(my_query)
    retrved_app_secret_code=(''.join(map(str, result.pop())))
    if retrved_app_secret_code == app_secret_code:
        return "True"
    else:
        return "False"
########################################## return logged userid to app #######################################

#this function must return related user id from session table that has session id and appcode 
def return_logged_user_id_to_app(session_id,app_id):
    my_query = "SELECT s_user_id FROM session_table WHERE session_id= '"+session_id+"' AND s_app_id= '"+app_id+"'"
    result=db.rert(my_query)
    user_id=(''.join(map(str, result.pop())))
    print (user_id)
    return user_id

############################################ send event to ESB #############################################



########################################### run G server ###################################################
# Run app
while True:
    sockett.start_listening(main_operator)
    
