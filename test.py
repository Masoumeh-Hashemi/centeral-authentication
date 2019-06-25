# Author: @Masoumeh-Hashemi
# Date: June 10 2019
# Description: Handles all network operations
import sqlite3
# import DB
import LAYER7
# import socket
import DB
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
    

#show sessio table
# db_instance.execute("INSERT INTO session_table( session_id,s_app_id,s_user_id) VALUES ('123txt','123txt','123txt')")
# register_user("123","1233")
# result=db_instance.rert("SELECT * FROM session_table")
# print(result)
# main_operation("credential")

byte_object= b"test" # byte object by literally typing characters
print(byte_object) # Prints b'test'
print(byte_object.decode('utf8')) # Prints "test" without quotations