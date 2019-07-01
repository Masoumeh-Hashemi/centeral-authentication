# Author: @Masoumeh-Hashemi
# Date: June 10 2019
# Description: Handles all network operations
import sqlite3
# import DB
import LAYER7
# import socket
import DB
import threading
import time
import socket
import DB
import LAYER7
import time
import datetime
from _thread import *
import threading
import string
# import G
host = "127.0.0.1"
port = 8082
test_socket = LAYER7.layer7(host, port)

# var = input("Please enter something: ")
# print("You entered: " + var)
# a="1"
# b="2"

db_instance = DB.db('database')
# db_instance.execute("INSERT INTO user_table( user_username,user_password,user_mail,user_mail_code) VALUES ('masoumeh','123456','mas@gmail.com','somecode')")
# db_instance.execute("INSERT INTO user_table( user_username,user_password) VALUES ('"+a+"','"+b+"')")

# result=db_instance.rert("SELECT * FROM user_table")

# my_query="SELECT * FROM user_table WHERE user_username= '"+a+"' AND user_password= '"+b+"'"
# my_query="SELECT * FROM user_table WHERE (user_username= '"+a+"' & user_password= '"+b+"')"
# result = db_instance.rert(my_query)

# result = db_instance.rert("SELECT * FROM user_table WHERE user_username=='1'")

# result=db_instance.rert("SELECT * FROM app_table")


# how to pick one app_code from table and convert it to string
# my_query="SELECT app_code FROM app_table WHERE app_name= 'golestanapp'"
# result=db_instance.rert(my_query)
# result=result[0]
# result=(''.join(map(str, result)))
# print(result)


# how to covert a list to string
# list=[]
# list.append("action")
# list.append(" ")
# list.append("requested_app")
# str1 = ''.join(list)
# print(str1)



# def register_user(session_id,s_app_id):
#     a=str(session_id)
#     b=str(s_app_id)
#     # my_query = 'INSERT INTO session_table (session_id,s_app_id) VALUES (\'a\',\'b\')'
#     my_query = 'INSERT INTO session_table (session_id,s_app_id) VALUES (\''+ a +'\',\'' + b + '\')'
#     db_instance.execute(my_query)
#     test_socket.send_request("credential",8082)

# def main_operation(inputt):
#     if inputt=="credential":
#         username=input("Please enter username: ")
#         password=input("Please enter password: ")
#         list=[]
#         list.append("enter_credential")
#         list.append(" ")
#         list.append(username)
#         list.append(" ")
#         list.append(password)
#         str1 = ''.join(list)
#         print(str1)
#         test_socket.send_request(str1,8080)

    # register_user("hghghf",6)
    
    # conn = sqlite3.connect('database.db')
    # conn.execute("INSERT INTO session_table (session_id,s_app_id) values (?, ?)", (a,b))
    # conn.execute("INSERT INTO session_table (session_id,s_app_id) VALUES (a,b)"
    # conn.commit()
    
# def credential(username,password):
    # my_query = "INSERT INTO user_table( user_username,user_password) VALUES ('"+username+"','"+password+"')"
    # db_instance.execute(my_query)
    # get_userid_query="SELECT user_id FROM user_table WHERE user_username= '"+username+"' AND user_password= '"+password+"'"
    # result=db_instance.rert(get_userid_query)
    # result=result[0]
    # result=(''.join(map(str, result)))
    # add_to_sessiontable_query="INSERT INTO session_table( s_user_id) VALUES ('"+result+"')"
    # db_instance.execute(add_to_sessiontable_query)
    # return ""

#show sessio table
# db_instance.execute("INSERT INTO session_table( session_id,s_app_id,s_user_id) VALUES ('123txt','123txt','123txt')")
# register_user("123","1233")
# result=db_instance.rert("SELECT * FROM session_table")
# print(result)
# main_operation("credential")
# print(credential("new user","mmmasss"))


# def fun1(a, b):
#     time.sleep(1)
#     c = a + b
#     print(c)
# thread1 = threading.Thread(target = fun1, args = (12, 10))
# thread1.start()
# thread2 = threading.Thread(target = fun1, args = (10, 17))
# thread2.start()
# print(“Total number of threads”, threading.activeCount())

# import socket, threading
# class ClientThread(threading.Thread):
#     def __init__(self,clientAddress,clientsocket):
#         threading.Thread.__init__(self)
#         self.csocket = clientsocket
#         print ("New connection added: ", clientAddress)
#     def run(self):
#         print ("Connection from : ", clientAddress)
#         #self.csocket.send(bytes("Hi, This is from Server..",'utf-8'))
#         msg = ''
#         while True:
#             data = self.csocket.recv(2048)
#             msg = data.decode()
#             if msg=='bye':
#               break
#             print ("from client", msg)
#             self.csocket.send(bytes(msg,'UTF-8'))
#         print ("Client at ", clientAddress , " disconnected...")
# LOCALHOST = "127.0.0.1"
# PORT = 8080
# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# server.bind((LOCALHOST, PORT))
# print("Server started")
# print("Waiting for client request..")
# while True:
#     server.listen(1)
#     clientsock, clientAddress = server.accept()
#     newthread = ClientThread(clientAddress, clientsock)
#     newthread.start()

# def check_app_secret_code(app_secret_code,app_code):
#     my_query="SELECT app_secret_code FROM app_table WHERE app_code ='"+app_code+"' "
#     result=db_instance.rert(my_query)
#     retrved_app_secret_code=(''.join(map(str, result.pop())))
#     if retrved_app_secret_code == app_secret_code:
#         print("done")
#         return True
#     else:
#         print("not done")
#         return False

# check_app_secret_code("12345678","3")
# def channel_id(appid):
#     my_query="SELECT app_channel_id FROM app_table WHERE app_code= '"+appid+"' "
#     channel_id_lists = db_instance.rert(my_query)
#     channel_id=channel_id_lists[0]
#     channel_id=(''.join(map(str, channel_id)))
#     print(channel_id)
#     str1 = appid +" "+ user_id + " " + channel_id
#     test_socket.send_request(str1,8083)
#     return ""

# channel_id("2")

# def pick_login_events(inputt):
#     my_query1="SELECT app_channel_id FROM app_table WHERE app_name=='"+inputt+"' "
#     result=db_instance.rert(my_query1)
#     channel_number=(''.join(map(str, result.pop())))
#     print(channel_number)

#     my_query2 = "SELECT channel_secret FROM esb_table WHERE channel_id=='"+channel_number+"' "
#     result2 = db_instance.rert(my_query2)
#     print(result2)
#     channel_secret="request_for_event "+(''.join(map(str, result2.pop())))
#     print(channel_secret)
#     return ""

# pick_login_events('golestanapp')

# channel_id="2"
# my_query="SELECT a_user_id FROM esb_assosiation_table WHERE a_channel_id='"+channel_id+"'"
# result1=db_instance.rert(my_query)

# list=[]
# for a_tuple in result1:  # iterates through each tuple
#     for item in a_tuple:  # iterates through each tuple items
#         list.append(item)
# print(list)
# str1 = ' '.join(str(e) for e in list)
# print(str1)


# def add_subscriber(app_secret_code1,channel_secret_id):
#         #should return boolean
#         # app give secret channel and esb 
#         my_query="SELECT app_code FROM app_table WHERE app_secret_code='"+app_secret_code1+"' "
#         result=db_instance.rert(my_query) 
#         retrived_app_code=(''.join(map(str, result.pop())))
#         print(retrived_app_code)

#         my_query="SELECT channel_id FROM esb_table WHERE channel_secret='"+channel_secret_id+"' "
#         result=db_instance.rert(my_query) 
#         retrived_channel_id=(''.join(map(str, result.pop())))
#         print(retrived_channel_id)
# # "UPDATE ExampleTable SET Age = 18 WHERE Age = 17"
#         my_query="UPDATE app_table SET app_channel_id='"+retrived_channel_id+"' WHERE app_code='"+retrived_app_code+"' "
#         db_instance.execute(my_query)
#         return "app added to channel"


# add_subscriber("59392564","fd819322a8fc4da6a706e51de5a05e6c")



# def subcribe_to_channel(appname,channelname):
#     my_query1="SELECT app_secret_code FROM app_table WHERE app_name =='"+appname+"' "
#     result=db_instance.rert(my_query1)
#     app_secret_code=result[0].__str__()
#     # app_secret_code=(''.join(map(str, result.pop())))
#     # app_secret_code=(''.join(map(str, result))
#     my_query2 = "SELECT channel_secret FROM esb_table WHERE channel_name =='"+channelname+"' "
#     result2 = db_instance.rert(my_query2)
#     # channel_secret_code= result2[0].__str__()
#     app_secret_code1=str.__str__(app_secret_code).strip('[]')
#     # channel_secret_code=(''.join(map(str, result2))
#     # channel_secret_code=(''.join(map(str, result2.pop())))


#     str="add_subscriber"+app_secret_code + channel_secret_code
#     print(str)
#     return "str"

# subcribe_to_channel("golestanapp","first channel")


def leave_channel(appname):
    my_query1="SELECT app_secret_code FROM app_table WHERE app_name=='"+appname+"' "
    result=db_instance.rert(my_query1)
    app_secret_code=(''.join(map(str, result.pop())))
    string_to_send="unsubscribe "+app_secret_code
    print(string_to_send)
    test_socket.send_request(string_to_send,8083)

leave_channel("refahi")
