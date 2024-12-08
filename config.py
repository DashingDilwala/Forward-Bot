import datetime
from os import environ 

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

class Config:
    API_ID = environ.get("API_ID", "27494535")
    API_HASH = environ.get("API_HASH", "52210cf4440a4a2b816ed1bcad615d4d")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7082109889:AAFlMZocuQFVNp9g6vJC5YBuNxQEL53yXDw") 
    BOT_SESSION = environ.get("BOT_SESSION", "Auto_Forward") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://forwardbot:forwardbot@cluster0.uqxlz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "Cluster0")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '5601277336').split()]
    LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002229340415'))
    FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "-1001948462404") 
    FORCE_SUB_ON = environ.get("FORCE_SUB_ON", "True")
    PORT = environ.get('PORT', '8080')
    
#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

   
class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 
