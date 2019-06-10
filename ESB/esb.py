import sys 
import os
os.system("C:/Users/Masoumeh/Documents/AuthProject/Project/USER/user1.py")
os.system("C:/Users/Masoumeh/Documents/AuthProject/Project/APP/app1.py")



class esb():
    channelID:""
    channelname:""
    channelsecret:int
    data:"#json string"
    
    #user class object
    #app class object

    def __init__(self,channelID,channelname):
        
        self.channelID=channelID
        self.channelname=channelname

    def SendUsers(self,Channelsecret,Appsecret):
        #it should return an array of userids 
        return user.user_id

    def AddSubscriber(self,Appsecret,Channelsecret):
        return bool

    def Delsubscriber(self,Appsecret,Channelsecret):
        return bool

    def SendData(self,channelID,Appcode):
        return esb.data