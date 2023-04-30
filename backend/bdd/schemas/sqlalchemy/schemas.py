from __future__ import annotations
from typing import List, Optional
from sqlalchemy import String, Integer, Float, Table, ForeignKey, Column, Text, BigInteger
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship

class Base(DeclarativeBase):
    """The base class for all models"""
    pass

has_watched = Table(
    "has_watched",
    Base.metadata,
    Column("user_id", ForeignKey("users.id"), primary_key=True),
    Column("movie_id", ForeignKey("movies.id"), primary_key=True),
)

class Movie(Base):
    """The sqlalchemy movie model, used to create the database 'movies' table"""
    __tablename__ = "movies"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    title: Mapped[str] = mapped_column(String(250))
    overview: Mapped[str] = mapped_column(Text)
    release_date: Mapped[str] = mapped_column(String(250))
    genres: Mapped[str] = mapped_column(String(250))
    vote_average: Mapped[float] = mapped_column(Float)
    popularity: Mapped[int] = mapped_column(Integer)
    poster_path: Mapped[Optional[str]] = mapped_column(String(250))
    users: Mapped[Optional[List[User]]] = relationship("User", secondary=has_watched, back_populates="movies")

    def __str__(self) -> str:
        return f"Movie(id={self.id}, title={self.title}, overview={self.overview}, release_date={self.release_date}, genres={self.genres}, vote_average={self.vote_average}, popularity={self.popularity}, poster_path={self.poster_path})"

has_team = Table(
    "has_team",
    Base.metadata,
    Column("user_id", ForeignKey("users.id"), primary_key=True),
    Column("team_id", ForeignKey("teams.id"), primary_key=True),
)

class User(Base):
    """The sqlalchemy user model, used to create the database 'users' table"""
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    firstname: Mapped[str] = mapped_column(String(50))
    lastname: Mapped[str] = mapped_column(String(50))
    username: Mapped[Optional[str]] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(50))
    password: Mapped[str] = mapped_column(String(50))
    profile_picture: Mapped[Optional[str]] = mapped_column(String(250))
    favorite_genres: Mapped[Optional[str]] = mapped_column(String(250))

    teams: Mapped[Optional[List[Team]]] = relationship("Team", secondary=has_team, back_populates="users")
    movies: Mapped[Optional[List[Movie]]] = relationship("Movie", secondary=has_watched,back_populates="users")

    def __str__(self) -> str:
        return f"User(id={self.id}, firstname={self.firstname}, lastname={self.lastname})"

class Team(Base):
    """The sqlalchemy team model, used to create the database 'teams' table"""
    __tablename__ = "teams"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))

    users: Mapped[Optional[List[User]]] = relationship("User", secondary=has_team, back_populates="teams")

    def __str__(self) -> str:
        return f"Team(id={self.id}, name={self.name})"
    
