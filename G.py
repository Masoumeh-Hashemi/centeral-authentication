# Author: @Masoumeh-Hashemi
# Date: June 10 2019
# Description: Handles all network operations

# Importing dependecies
import socket
import DB
import LAYER7

# Define constrains
host = "127.0.0.1"
port = 8080

# Initialize classes
db = DB.db("G.db")
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
    db.execute("INSERT INTO USERS (USERNAME, PASSWORD) VALUES ('A','B')")
    return "You are going to register " + username + " with pass: " + password

# login function
def login(username, password):
    result = db.rert("SELECT 'A'")
    return "You are going to login with " + username + " and pass: " + password

# Run app
sockett.start_listening(main_operator)