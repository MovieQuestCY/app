from __future__ import annotations
from pydantic import BaseModel

class TeamBase(BaseModel):
    """The base team model"""
    name: str

class TeamCreate(TeamBase):
    user_id: int
    pass

class Team(TeamBase):
    """The team model for returning a team"""
    id: int

    class Config:
        """The config for the team model"""
        orm_mode = True