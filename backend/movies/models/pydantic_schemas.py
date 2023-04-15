from __future__ import annotations
from typing import List
from pydantic import BaseModel

class MovieBase(BaseModel):
    """The base movie model"""
    id: int
    title: str
    overview: str
    release_date: str
    genres: str
    vote_average: float
    popularity: int
    poster_path: str

class MovieCreate(MovieBase):
    """The movie model for creating a new movie"""
    pass

class Movie(MovieBase):
    """The movie model for returning a movie"""
    class Config:
        """The config for the movie model"""
        orm_mode = True
