from __future__ import annotations
from typing import Optional
from pydantic import BaseModel

class PUserBase(BaseModel):
    """The base user model"""
    firstname: str
    lastname: str
    username: Optional[str]
    email: str
    profile_picture: Optional[str]
    favorite_genres: Optional[str]

class PUserLogin(BaseModel):
    """The user model for logging in a user"""
    email: str
    password: str

class PUserCreate(PUserBase):
    """The user model for creating a new user"""
    password: str

class PUser(PUserBase):
    """The user model for returning a user"""
    id: int

    class Config:
        """The config for the user model"""
        orm_mode = True

class PUserLogged(PUser):
    """The user model for returning a user after creation"""
    token: str

