from __future__ import annotations
from typing import Optional
from pydantic import BaseModel

class PMovieBase(BaseModel):
    """The base movie model"""
    id: int
    title: str
    overview: str
    release_date: str
    genres: str
    vote_average: float
    popularity: int
    poster_path: Optional[str]

class PMovieCreate(PMovieBase):
    """The movie model for creating a new movie"""
    pass

class PMovie(PMovieBase):
    """The movie model for returning a movie"""
    class Config:
        """The config for the movie model"""
        orm_mode = True
