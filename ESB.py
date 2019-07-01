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
dbname = 'database.db'
host = "127.0.0.1"
port = 8083

# Initialize classes
db = DB.db('database.db')
esb_socket = LAYER7.layer7(host, port)
db = DB.db(dbname)

class esb:
    #attributes
    
    channel_id:int
    channel_secret_id:int
    channel_name:str
    data:str

    #functions
    
    # def __init__(self,Appname):
    #     self.app_name=Appname

    def send_users(self,channel_id,app_secret_code):
         #send list of users to who ask for it and should return a list
         pass

    def add_subscriber(self,app_secret_code,channel_secret_id):
        #should return boolean
        pass
    def delete_subscriber(self,app_secret_code,channel_secret_id):
        #delete a subscriber and should return boolean
        pass
    def send_data(self,channel_id,appcode): 
        #shold send data in response
        pass
    
    #receive event from G and save to assosiation table and it need channel id,app,id,user id
    def receive_login_event(self,app_id,user_id,channel_id):
        my_query = "INSERT INTO esb_assosiation_table (a_app_code,a_user_id,a_channel_id) VALUES ('"+app_id+"','"+user_id+"','"+channel_id+"')"
        db.execute(my_query)
        print( "new user with userid:" + user_id + " Loged in"  )
        return "event added"



def main_operator(input):
    if input[0] == "login_event":
        #appid userid channelid
        esb_instance= esb()
        return esb_instance.receive_login_event(input[1],input[2],input[3])


esb_socket.start_listening(main_operator)