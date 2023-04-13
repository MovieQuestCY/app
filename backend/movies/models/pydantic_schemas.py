from __future__ import annotations
from typing import List
from pydantic import BaseModel

class MovieBase(BaseModel):
    """The base movie model"""
    title: str
    description: str
    year: int
    genre: List[str]
    director: str

class MovieCreate(MovieBase):
    """The movie model for creating a new movie"""
    pass

class Movie(MovieBase):
    """The movie model for returning a movie"""
    id: int

    class Config:
        """The config for the movie model"""
        orm_mode = True
