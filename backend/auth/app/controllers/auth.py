from app.models.db import Database
from sqlalchemy import text

from backend.auth.app.db import SessionLocal
from ..models.pydantic_schemas import TokenData, User, UserCreate
from backend.users.controllers.users import get_user,get_user_by_email
import bcrypt

from datetime import datetime, timedelta
from typing import Annotated

from jose import JWTError, jwt
from passlib.context import CryptContext

from typing import Union

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing_extensions import Annotated

def get_db():
    """Get a database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def check_password(email: str,password: str):
    user = await get_user_by_email(Session = Depends(get_db), email = email)
    if user is None:
        return False
    elif bcrypt.checkpw(password, user.password):
        return True
    return False

# def decode_token(token):
#     #TODO : decode token
#     return(0)


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(Session = Depends(get_db), username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)]
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user