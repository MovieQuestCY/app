from __future__ import annotations
from typing import Optional, List
from pydantic import BaseModel

class UserBase(BaseModel):
    """The base user model"""
    firstname: str
    lastname: str
    username: Optional[str]
    email: str
    profile_picture: Optional[str]
    favorite_genres: Optional[str]

class UserLogin(BaseModel):
    """The user model for logging in a user"""
    email: str
    password: str

class UserCreate(UserBase):
    """The user model for creating a new user"""
    password: str

class User(UserBase):
    """The user model for returning a user"""
    id: int

    class Config:
        """The config for the user model"""
        orm_mode = True

class UserLogged(User):
    """The user model for returning a user after creation"""
    token: str

