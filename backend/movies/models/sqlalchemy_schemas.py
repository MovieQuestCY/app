from __future__ import annotations
from typing import List
from sqlalchemy import String, Integer, Float
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase

class Base(DeclarativeBase):
    """The base class for all models"""
    pass

class Movie(Base):
    """The sqlalchemy movie model, used to create the database 'movies' table"""
    __tablename__ = "movies"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(250))
    overview: Mapped[str] = mapped_column(String(250))
    release_date: Mapped[str] = mapped_column(String(250))
    genres: Mapped[str] = mapped_column(String(250))
    vote_average: Mapped[float] = mapped_column(Float)
    popularity: Mapped[int] = mapped_column(Integer)
    poster_path: Mapped[str] = mapped_column(String(250))

    def __str__(self) -> str:
        return f"Movie(id={self.id}, title={self.title}, overview={self.overview}, release_date={self.release_date}, genres={self.genres}, vote_average={self.vote_average}, popularity={self.popularity}, poster_path={self.poster_path})"

