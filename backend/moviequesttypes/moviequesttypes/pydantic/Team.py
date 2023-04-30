from __future__ import annotations
from pydantic import BaseModel

class PTeamBase(BaseModel):
    """The base team model"""
    name: str

class PTeamCreate(PTeamBase):
    user_id: int
    pass

class PTeam(PTeamBase):
    """The team model for returning a team"""
    id: int

    class Config:
        """The config for the team model"""
        orm_mode = True