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
    if input[0] == "register_app":
        return register_user(input[1], input[2])
    elif input[0] == "login_app":
        return login_user(input[1], input[2])
    #TODO:باید if تو در تو بنویسم برای حالت user
    else:
        return "Command not found"
############################################## User##################################################
# regsiter function
def register_user(username, password):
    a=username
    b=password
    my_query = "INSERT INTO user_table( user_username,user_password) VALUES ('"+a+"','"+b+"')"
    db.execute(my_query)
    return print("You are going to register " + username + " with pass: " + password)

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

################################################App##################################################
#create random string for app_secret_code
def generate_random_string():
    stringLength = 8
    randomString = uuid.uuid4().hex # get a random string in a UUID fromat
    randomString  = randomString.upper()[0:stringLength] # convert it in a uppercase letter and trim to your size.
    return randomString

    
#register App function and return secret_app_code to the app who called it   
def register_app(appname, url):
    a=appname
    b=url
    c=generate_random_string()
    my_query = "INSERT INTO app_table( app_secret_code,app_name,app_url) VALUES ('"+c+"','"+a+"','"+b+"')"
    db.execute(my_query)
    print("App " + a + " registered with URL: " + b)   
    return c

     
register_app('app1','me.com')
# Run app
sockett.start_listening(main_operator)
