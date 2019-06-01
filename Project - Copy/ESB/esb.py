from APP.app1 import *
from USER.user1 import *





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
        return user.UserID

    def AddSubscriber(self,Appsecret,Channelsecret):
        return bool

    def Delsubscriber(self,Appsecret,Channelsecret):
        return bool

    def SendData(self,channelID,Appcode):
        return esb.data