# Author: @Masoumeh-Hashemi
# Date: June 10 2019
# Description: esb part

# Importing dependecies
import socket
import DB
import LAYER7
import time
import datetime



# Define constrains
host = "127.0.0.1"
port = 8083

# Initialize classes
db = DB.db('database.db')
app_socket = LAYER7.layer7(host, port)

class esb:
    #attributes
    
    channel_id:int
    channel_secret_id:int
    channel_name:str
    data:str

    #functions
    
    def __init__(self,Appname):
        self.app_name=Appname