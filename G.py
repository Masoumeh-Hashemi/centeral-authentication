# Author: @Masoumeh-Hashemi
# Date: June 10 2019
# Description: Handles all network operations

# Importing dependecies
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
    if input[0] == "register":
        return register(input[1], input[2])
    elif input[0] == "login":
        return login(input[1], input[2])
    else:
        return "Command not found"

# regsiter function
def register(username, password):
    a=username
    b=password
    my_query = "INSERT INTO user_table( user_username,user_password) VALUES ('"+a+"','"+b+"')"
    db.execute(my_query)
    return print("You are going to register " + username + " with pass: " + password)

# login function
def login(username, password):
    a=username
    b=password
    my_query="SELECT * FROM user_table WHERE (user_username== '"+a+"' & user_password== '"+b+"') "
    result = db.rert(my_query)
    # if not result:
    #     print("wrong username or password")
    # return "You are going to login with  '"+ a +"'  and pass:  '"+ b +"' "
    print(result)
    # return result
    
    
        


register('user1','password1')   
login('user1','password1')        

# Run app
sockett.start_listening(main_operator)
# login('masoumeh','123456')  