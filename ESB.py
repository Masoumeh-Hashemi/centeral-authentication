# Author: @Masoumeh-Hashemi
# Date: June 10 2019
# Description: esb part

# Importing dependecies
import socket
import DB
import LAYER7
import time
import datetime
import uuid



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

    ############################################ send events to apps #################################
    #send list of users to who ask for it and should return a list
    # at first with secret channel code ,retrive the channel number and then ,in event table return all the users on that channel
    def send_events_to_apps(self,channel_secret1):
         my_query= "SELECT channel_id FROM esb_table WHERE channel_secret='"+channel_secret1+"'"
         result=db.rert(my_query)
         channel_id=(''.join(map(str, result.pop())))
         print(channel_id)
         my_query="SELECT a_user_id FROM esb_assosiation_table WHERE a_channel_id='"+channel_id+"'"
         result1=db.rert(my_query)
         list=[]
         for a_tuple in result1:  # iterates through each tuple
             for item in a_tuple:  # iterates through each tuple items
                 list.append(item)
         str1 = ' '.join(str(e) for e in list)
         return str1


######################################### add subscriber to a channel ####################################
# TODO:APP part has been left,should test them together
    def add_subscriber(self,app_secret_code1,channel_secret_id):
        #should return boolean
        # app give secret channel and esb 
        my_query="SELECT app_code FROM app_table WHERE app_secret_code='"+app_secret_code1+"' "
        result=db.rert(my_query) 
        retrived_app_code=(''.join(map(str, result.pop())))

        my_query="SELECT channel_id FROM esb_table WHERE channel_secret='"+channel_secret_id+"' "
        result=db.rert(my_query) 
        retrived_channel_id=(''.join(map(str, result.pop())))
        my_query="UPDATE app_table SET app_channel_id='"+retrived_channel_id+"' WHERE app_code='"+retrived_app_code+"' "
        db.execute(my_query)
        return "app added to channel"


######################################## delete subsciber ################################################

    def delete_subscriber(self,app_secret_code1):
        #delete a subscriber and should return boolean
        my_query="SELECT app_code FROM app_table WHERE app_secret_code=='"+app_secret_code1+"' "
        result=db.rert(my_query) 
        retrived_app_code=(''.join(map(str, result.pop())))
        my_query="UPDATE app_table SET app_channel_id='' WHERE app_code=='"+retrived_app_code+"' "
        db.execute(my_query)
        return "app deleted from channel"

###################################### send data #########################################################

    def send_data(self,channel_id,appcode): 
        #shold send data in response
        pass
    
###################################### and a new channel to esb ##########################################
    #add new channel to channel lists
    def create_channel_for_esb(self,channel_name):
        channel_secret_code = uuid.uuid4().hex 
        my_query="INSERT INTO esb_table (channel_name,channel_secret) VALUES ('"+channel_name+"','"+channel_secret_code+"')"
        db.execute(my_query)

###################################### receive login event ##############################################
    #receive event from G and save to assosiation table and it need channel id,app,id,user id
    def receive_login_event(self,app_id,user_id,channel_id):
        my_query = "INSERT INTO esb_assosiation_table (a_app_code,a_user_id,a_channel_id) VALUES ('"+app_id+"','"+user_id+"','"+channel_id+"')"
        db.execute(my_query)
        print( "new user with userid:" + user_id + " Loged in"  )
        return "event added"


########################################### main operator ###############################################


def main_operator(input):
    if input[0] == "login_event":
        #appid userid channelid
        esb_instance= esb()
        return esb_instance.receive_login_event(input[1],input[2],input[3])

    if input[0] == "request_for_event":
        esb_instance= esb()
        #input[1]=channelsecret code
        return esb_instance.send_events_to_apps(input[1])

    if input[0] == "add_subscriber":
        esb_instance= esb()
        #input[1]=app_secret_code
        #input[2]=channel_secret_code
        return esb_instance.add_subscriber(input[1],input[2])

    if input[0] == "unsubscribe":
        esb_instance= esb()
        #input[1]=app_secret_code
        return esb_instance.delete_subscriber(input[1])

    # elif:
    #     print("command not found")
########################################### start esb ###############################################
test_esb= esb()
# test_esb.create_channel_for_esb("second channel")
esb_socket.start_listening(main_operator)