from fastapi import APIRouter
from sqlalchemy import create_engine
from models.users import User
from controllers.auth import check_password, create_user, get_user
# import jwt
import os

SECRET_KEY = os.getenv('secret_key_test', 'my_precious')


router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Hello World"}

@router.get("login")
async def connectUser(email: str, password: str):
    if(check_password(email, password)):
        return {"message": "Invalid password"}
    else:
        return {"message": f"Welcome {email}"}

@router.get("register")
async def newUser(email: str, password: str):
    #insert into database
    newUser = User(email=email, password=password)
    create_user(newUser)
    return {"message": f"Welcome {email}"}

@router.get("lougout")
async def disconnectUser():
    return {"message": "Goodbye"}
