import jwt
from config import Config
import pytz
import datetime

class Token:
    key = Config.SECRET_KEY
    tz = pytz.timezone("America/Asuncion")
    
    @classmethod    
    def generar_token (cls,user_data):
        
        payload = {
            "iat": datetime.datetime.now(tz=cls.tz),
            "exp": datetime.datetime.now(tz=cls.tz)+ datetime.timedelta (minutes=10),
            "username": user_data.username
        }
        token = jwt.encode(payload,cls.key,algorithm="HS256")
    
        return token
    
    @classmethod
    def verificar_token (cls,token):
        try:
            payload = jwt.decode(token,cls.key,algorithms="HS256")
            if payload:
                return True
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None
        
            
        
         