# Author: @Masoumeh-Hashemi
# Date: June 10 2019
# Description: create tables in sqlite

import sqlite3

conn=sqlite3.connect('database.db')
conn.execute("PRAGMA foreign_keys = 1")
c=conn.cursor()
# c.execute("PRAGMA foreign_keys = ON")
################################### user table #######################################
c.execute("""CREATE TABLE user_table (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_username text,
    user_password text,
    user_mail text,
    user_mail_code text
    )""")

################################App table #################################
c.execute("""CREATE TABLE app_table (
            app_code INTEGER PRIMARY KEY AUTOINCREMENT,
            app_secret_code text,
            app_name text,
            app_url text,
            user_confirm text,
            app_channel_id integer,
            FOREIGN KEY(app_channel_id) REFERENCES esb_table(channel_id)
    )""")

#####################################Session table##############################
c.execute("""CREATE TABLE session_table( 
                session_id text,
                s_app_id integer,
                s_user_id integer,
                FOREIGN KEY(s_app_id) REFERENCES app_table(app_code),
                FOREIGN KEY(s_user_id) REFERENCES user_table(user_id)
    )""")

    
 ######################################ESB table##########################################
c.execute("""CREATE TABLE esb_table( 
            channel_id INTEGER PRIMARY KEY AUTOINCREMENT,
            channel_name text,
            channel_secret text,
            esb_data json,
            discrption text,
            date_time time
    )""")



#######################################ESB association table################################

c.execute("""CREATE TABLE esb_assosiation_table( 
    a_app_code integer,
    a_channel_id integer,
    a_user_id integer,
    FOREIGN KEY(a_app_code) REFERENCES app_table(app_code),
    FOREIGN KEY(a_channel_id) REFERENCES esb_table(channel_id),
    FOREIGN KEY(a_user_id) REFERENCES user_table(user_id)
    )""")
conn.close()
