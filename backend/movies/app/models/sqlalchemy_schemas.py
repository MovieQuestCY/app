from __future__ import annotations
from typing import List, Optional
from sqlalchemy import String, Column, Table, ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column, DeclarativeBase

class Base(DeclarativeBase):
    """The base class for all models"""
    pass

class Movie(Base):
    """The sqlalchemy movie model, used to create the database 'movies' table"""
    __tablename__ = "movies"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(250))
    year: Mapped[int] = mapped_column(int)
    genre: Mapped[List[str]] = mapped_column(String(50))
    director: Mapped[str] = mapped_column(String(250))

    def __str__(self) -> str:
        return f"Movie(title={self.title}, year={self.year}, genre={self.genre}, director={self.director})"

