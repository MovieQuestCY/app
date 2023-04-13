from __future__ import annotations
from typing import List
from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase

class Base(DeclarativeBase):
    """The base class for all models"""
    pass

class Movie(Base):
    """The sqlalchemy movie model, used to create the database 'movies' table"""
    __tablename__ = "movies"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(250))
    description: Mapped[str] = mapped_column(String(250))
    year: Mapped[int] = mapped_column(Integer)
    genre: Mapped[List[str]] = mapped_column(String(250))
    director: Mapped[str] = mapped_column(String(250))

    def __str__(self) -> str:
        return f"Movie(title={self.title}, year={self.year}, genre={self.genre}, director={self.director})"

