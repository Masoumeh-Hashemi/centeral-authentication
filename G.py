# Author: @Masoumeh-Hashemi
# Date: June 10 2019
# Description: Handles all network operations

# Importing dependecies
import socket
import DB

# Define constrains
host = "127.0.0.1"
port = 8080

# Initialize classes
db = DB.db("G.db")

# Application functionality
def main_operator(input):
    if input[0] == "register":
        print (db.execute("INSERT INTO USERS (USERNAME, PASSWORD) VALUES ('A','B')"))
        return register(input[1], input[2])
    elif input[0] == "login":
        return login(input[1], input[2])
    else:
        return "Command not found"

# regsiter function
def register(username, password):
    return "You are going to register " + username + " with pass: " + password

# login function
def login(username, password):
    return "You are going to login with " + username + " and pass: " + password


# Application main thread
def main():

    # Listen network
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv.bind((host, port))
    serv.listen(5)

    # Network stuff
    while True:
        # Accept packets
        conn, addr = serv.accept()
        # Recieve data
        data_ready = ''
        while True:
            data = conn.recv(4096)
            if not data: break
            data_ready += str(data, encoding = "UTF-8")
        # Call operator
        input_array = data_ready.split(' ')
        result = main_operator(input_array)
        print (result)
        # Return result to clientc
        conn.sendall(bytes(result, encoding = "UTF-8"))
        # Close connection
        conn.close()

# Run app
main()