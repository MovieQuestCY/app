from __future__ import annotations
from typing import Optional
from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

class UserBase(BaseModel):
    """The base user model"""
    firstname: str
    lastname: str
    username: Optional[str]
    email: str
    profile_picture: Optional[str]

class UserCreate(UserBase):
    """The user model for creating a new user"""
    password: str

class User(UserBase):
    """The user model for returning a user"""
    id: int

    class Config:
        """The config for the user model"""
        orm_mode = True

class TeamBase(BaseModel):
    """The base team model"""
    name: str

class TeamCreate(TeamBase):
    pass

class Team(TeamBase):
    """The team model for returning a team"""
    id: int

    class Config:
        """The config for the team model"""
        orm_mode = True