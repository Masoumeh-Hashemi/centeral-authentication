import os
import sys 
import subprocess
import random
import string
import datetime
import sys 
import os
# os.system("C:\Users\Masoumeh\Documents\AuthProject\Project\DB\db.py")
# from DB.db import *
# from pathlib import Path
# sys.path.append("C:\Users\Masoumeh\Documents\AuthProject\Project\DB\db.py")
sys.path.append(r'C:\Users\Masoumeh\Documents\AuthProject\Project\DB')
# print(sys.path)
# import db
from db import *
# import db.py
# from ..DB import db
# from DB.db import *


class user():
        user_id=int
        user_password=""
        user_username=""

        def __init__(self,Username,Password):
                self.user_username=Username
                self.user_password=Password

        def Login(self,Username,Password):
                pass 
                #and also return boolean
                # return user.user_id
        def register_user(self,username,password):
               
                password=input("please enter username: ")
                username=input("please enter password: ")

                self.user_username=username
                self.user_password=password
                 

def create_new_user():
        user1=user("Username","password")
        user1.register_user("Username","password")
        # insert_user(user1)
        
        # val1 = input("Enter your username: ") 
      #  print('val1')
        # val2 = input("Enter your password: ") 
      #  print('val2')

# mypath = Path().absolute()
# print(mypath)
# var1=os.getcwd()
# print(var1)
# print(os.getcwd())
# print(sys.path())
# sys.path

