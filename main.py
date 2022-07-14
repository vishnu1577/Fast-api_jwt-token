#main api is the main entry point of our application

from fastapi import FastAPI,Body,Depends
import uvicorn
from app.model import PostSchema
from app.model import PostSchema,UserSchema,UserLoginSchema
from app.auth.jwt_handler import  signJWT
from app.auth.jwt_bearer import jwtBearer


#list of entries or post in the form of name and address                       
                
posts= [{"id":1, "name":"santosh", "address":"nashik"},{"id":2,"name":"mukesh", "address":"uttarkahand 45."}, 
    {"id":3,"name":"mandeep","address":"5-punjab ." }, {"id":4,"name":"Ranjeet", "address":"Punjab xy-90."},] 

       
users=[]                                       #users list, its initially empty and we will add the entry based on availability
 
app=FastAPI()                               #instances fast api application,main application of fastapi class

@app.get("/",tags=["Status"])#decorator for my main application, get route to homa page with tags or group of name [" "]
def SoftProdigy():          #creating function 
    return{"message":"Hello welcome to softprodigy, best!!!"}
#now here after we are collecting all post/single post 
#get posts
@app.get("/posts",tags=["posts"])
def get_posts():
    return{"data":posts}

#Get single post
@app.get("/posts/{id}",tags=["posts"])
def get_one_posts(id:int):
    if id>len(posts):
        return{
            "error":"post with the said id does not exist!!!"
        }
    for post in posts:
            if post["id"]==id:
                return{
                    "data":post
                }

    return{"message":"Hello welcome to softprodigy, best!!!"}
#post a blog [created by handler]
@app.post("/posts",dependencies=[Depends(jwtBearer())],tags=["posts"])
def add_post(post:PostSchema):
    post.id=len(posts)+1
    posts.append(post.dict())
    return{
        "info":"post added!"
    }


#user signup/create new user
@app.post("/user/signup",tags=["users"])
def user_signup(user:UserSchema=Body(default=None)):
    users.append(user)
    return  signJWT(user.email)

def check_user(data:UserLoginSchema):
    for user in users:
        if user.email==data.email and user.password==data.password:
            return True
        return False

#user login is ok or not
@app.post("/user/login",tags=["user"])
def user_login(user:UserLoginSchema=Body(default=None)):
    if check_user(user):
        return signJWT(user.email)
    else: 
            return {
                "error":"invalid login details"
            }