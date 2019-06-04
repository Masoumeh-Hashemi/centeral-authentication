import sqlite3
from USER.user1 import user
from APP.app1 import app


conn=sqlite3.connect('user.db')
c=conn.cursor()
c.execute("PRAGMA foreign_keys = ON")
####################### user table #######################################
c.execute("""CREATE TABLE user_table (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_username text,
    user_password text,
    user_mail text,
    user_mail_code text

    )""")

def insert_user(user):
    conn=sqlite3.connect('user.db')
    c=conn.cursor()
    with conn:
        c.execute("INSERT INTO user_table VALUES (?,?,?,?)",(user.user_username,user.user_password,user.user_mail,user.user_mail_code))
    conn.close()

def remove_user(user):
    conn=sqlite3.connect('user.db')
    c=conn.cursor()
    with conn:
        c.execute("DELETE from user_table WHERE user_username=?",(user.user_username,) )
    conn.close()
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

def insert_app(app):
    conn=sqlite3.connect('user.db')
    c=conn.cursor()
    with conn:
        c.execute("INSERT INTO app_table VALUES (?,?,?)",(app.app_secret_code,app.app_name,app.app_url))
    conn.close()
def remove_app(app):
    conn=sqlite3.connect('user.db')
    c=conn.cursor()
    with conn:
        c.execute("DELETE from app_table WHERE app_secret_code=?,app_name=?,app_url=?",(app.app_secret_code,app.app_name,app.app_url) )
    conn.close()
#####################################Session table##############################
c.execute("""CREATE TABLE session_table( 
                session_id text )""")

def insert_session(session):
    conn=sqlite3.connect('user.db')
    c=conn.cursor()
    with conn:
        c.execute("INSERT INTO session_table VALUES (?)",(session.session_id,))
    conn.close()
def remove_session(session):
    conn=sqlite3.connect('user.db')
    c=conn.cursor()
    with conn:
        c.execute("DELETE from session_table WHERE session_id=?,app_name=?",(session.session_id,) )
    
 ######################################ESB table##########################################
c.execute("""CREATE TABLE esb_table( 
            channel_id INTEGER PRIMARY KEY AUTOINCREMENT,
            channel_name text,
            channel_secret text,
            esb_data json,
            discrption text,
            date_time time

                 )""")

# functions


#######################################ESB association table################################

c.execute("""CREATE TABLE esb_assosiation_table( 
    a_app_code integer,
    a_channel_id integer,
    a_user_id integer,
    FOREIGN KEY(a_app_id) REFERENCES app_table(app_code),
    FOREIGN KEY(a_channel_id) REFERENCES esb_table(channel_id),
    FOREIGN KEY(a_user_id) REFERENCES user_table(user_id)

    )""")
conn.close()


    

conn.close()
