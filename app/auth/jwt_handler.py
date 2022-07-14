#This file is for signin,encoding and decoding the token based on algorithm

import time                     #As every token have expiry time
import jwt                      #encoding and decoding module for token
from decouple import config     #allow to change your settings with redploying the application,it also help you to store parameter in ini or .env file for record

JWT_SECRET=config("secret")
JWT_ALGORITHM=config("algorithm")

#function return the genrated token
def token_response(token:str):
    return{
        "access token":token
    }
    #signing the jwt token
def signJWT(userID:str):
    payload={
        "userId":userID,
        "expiry":time.time()+600
    }
    token=jwt.encode(payload,JWT_SECRET,algorithm=JWT_ALGORITHM)
    return token_response(token)


    #decode the token with the help of JWT module

def decodeJWT(token:str):
    try:
            decode_token=jwt.decode(token,JWT_SECRET,algorithm=JWT_ALGORITHM)
            return decode_token if decode_token['expires']>=time.time() else None
    except:
            return {}
    

    