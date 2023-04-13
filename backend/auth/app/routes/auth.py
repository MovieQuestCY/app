from fastapi import APIRouter
from pydantic import BaseModel
from app.models.users import User
from app.controllers.auth import check_password, create_user, get_user
from db import SessionLocal

from datetime import datetime, timedelta
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext

SECRET_KEY = "162679ef81a1575515486aaf5adde49496a9d1d1288c1aaf257a034e14f5680e"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

class Token(BaseModel):
    access_token: str
    token_type: str


class UserInDB(User):
    hashed_password: str


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter(prefix="/auth")

# Dependency
def get_db():
    """Get a database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
async def root():
    return {"message": "Auth api"}

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

@router.get("logout")
async def disconnectUser():
    return {"message": "Goodbye"}
