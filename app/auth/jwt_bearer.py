#securing the routes or protecting the routes from access,by checking request is authorize or not,
# fast api provides basic validation in the form of httpbearer class, in order to extract or parse the token
from pickle import FALSE
from fastapi import Request,HTTPException
from fastapi.security import HTTPBearer,HTTPAuthorizationCredentials
from .jwt_handler import decodeJWT

class jwtBearer(HTTPBearer):                #subclass of httpbearer class, for authentication the routes
    def __init__(self,auto_Error:bool=True):
        super(jwtBearer,self).__init__(auto_error=auto_Error)
        async def __call__(self,request:Request):                   #call method of bearer (creditional of the bearer of the token)
            creaditials:HTTPAuthorizationCredentials=await super(jwtBearer,self).__call__(request)
            if creaditials:
                if not creaditials.scheme=="Bearer":
                    raise HTTPException(status_code=403, details="Invalid or expired token")
                return creaditials.credentials
            else:raise HTTPException(status_code=403, details="Invalid or expired Token")


    def verify_jwt(self,jwtoken:str):
        isTokenValid:bool=False
        payload=decodeJWT(jwtoken)
        if payload:
            isTokenValid=True
            return isTokenValid