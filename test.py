# Author: @Masoumeh-Hashemi
# Date: June 10 2019
# Description: Handles all network operations
import sqlite3
import DB
import LAYER7

db_instance = DB.db('database')
db_instance.execute("INSERT INTO user_table VALUES (?,?,?,?)",(masoumeh,1234,a@yahoo.com,some random code))

