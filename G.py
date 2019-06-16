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
        return register_user(input[1], input[2])
        
    elif input[0] == "login_user":
        return login_user(input[1], input[2])

    elif input[0] == "register_app":
        c= register_app(input[1], input[2])
        return c
    elif input[0] == "enter_credential":
        return credential(input[1], input[2])
   
    else:
        print("command not found")
############################################## User##################################################
# regsiter function,at first it receives an session_id and app_id from requsted user and ask for credentials
def register_user(session_id,s_app_id):
    my_query = " INSERT INTO session_table(session_id,s_app_id) VALUES ('"+session_id+"' '"+s_app_id+"') "
    db.execute(my_query)
    sockett.send_request("credential",8082)
    # return s_app_id

#user enter credencials (usernmae and password) to be add in users table
def credential(username,password):
    my_query = "INSERT INTO user_table( user_username,user_password) VALUES ('"+username+"','"+password+"')"
    db.execute(my_query)
    print( "You are going to register " + username + " with pass: " + password )
    return ""

# login function
def login_user(username, password):
    a=username
    b=password
    
    my_query="SELECT * FROM user_table WHERE user_username= '"+a+"' AND user_password= '"+b+"'"
    result = db.rert(my_query)
    if not result:
        print("wrong username or password")
    if result:    
       print("You are going to login with  '"+ a +"'  and pass:  '"+ b +"' ") 
    return ""

################################################App##################################################
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
    #TODO:i want send this result to app
    # sockett.send_request(c,8081)
    # print(c)
    return c



# Run app
while True:
    sockett.start_listening(main_operator)
