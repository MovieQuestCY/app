from __future__ import annotations
from typing import List, Optional
from sqlalchemy import String, Column, Table, ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column, DeclarativeBase

class Base(DeclarativeBase):
    """The base class for all models"""
    pass

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

    teams: Mapped[Optional[List[Team]]] = relationship("Team", secondary=has_team, back_populates="users")

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
    
