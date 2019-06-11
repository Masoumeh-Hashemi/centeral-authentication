# Author: @Masoumeh-Hashemi
# Date: June 10 2019
# Description: working with database
import sqlite3

class db:

    DBNAME = ''

    def __init__(self, name):
        # TODO: init database connection with name passed
        self.DBNAME = name

    def rert(self, query):

        conn=sqlite3.connect('database.db')
        c=conn.cursor() 
        query_to_run=query
        c.execute(query_to_run)
        conn.commit()
        result=c.fetchall()
        print(result)
        return "Result"

    def execute(self, query):
        
        conn=sqlite3.connect('database.db')
        c=conn.cursor() 
        query_to_run=query
        c.execute(query_to_run)
        conn.commit()
        conn.close()
       