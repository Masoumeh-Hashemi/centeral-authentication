class app:
    #attributes
    app_code: int 
    app_name: ""
    app_url:""
    app_secret_code: ""

    #functions
    
    def __init__(self,Appname):
        self.app_name=Appname
        

    def Handshake(self,app_name,app_secret_code):
        #should return bool ,appcode
        return app.app_code
