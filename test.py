# Author: @Masoumeh-Hashemi
# Date: June 10 2019
# Description: Handles all network operations
import sqlite3
import DB
import LAYER7

db_instance = DB.db('database')
# db_instance.execute("INSERT INTO user_table( user_username,user_password,user_mail,user_mail_code) VALUES ('masoumeh','123456','mas@gmail.com','somecode')")
# db_instance.rert("SELECT * FROM user_table")
a="1"
b="2"
my_query="SELECT * FROM user_table WHERE (user_username=" +a+ "& user_password=" +b+")"
# result = db_instance.rert("SELECT * FROM user_table WHERE user_username=='1'")
result = db_instance.rert(my_query)

print(result)