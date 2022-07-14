#importing skeleton for different fields
from pydantic import BaseModel,Field,EmailStr


#class for diffrent posts or post schemas
class PostSchema(BaseModel):
    id:int=Field(default=None)
    name:str=Field(default=None)      #how the post schmea seems to be configured/formatted
    address:str=Field(default=None)
    phone_number:int=Field(default=None)
    class Config:                       #subclass
        schema_extra={                  #objects or dictionary
            "post_details":{
                "name":"name of the person",
                "adress":"Address of the person"                    
                }
            }


#Schems for handling registration and login

class UserSchema(BaseModel):
    fullname:str=Field(default=None)
    password:str=Field(default=None)
    email:EmailStr =Field(default=None)
    class config:
        schema_extra={
        "user_demo":{
            "name":"san",
            "email":"san@gmail.com",
            "password":"123"
        }
    }


class UserLoginSchema(BaseModel):
    password:str=Field(default=None)
    email:EmailStr =Field(default=None)
    class config:
        schema_extra={
            "user_demo":{
            "email":"san@gmail.com",
            "password":"123"
        }
    }