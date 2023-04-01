from fastapi import APIRouter, Depends
from app.models.db import Database
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.models.users import User
import bcrypt

from backend.users.app.db import SessionLocal

user_router = APIRouter(prefix="/auth")


def get_db():
    """Get a database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

async def get_user(email, db: Session = Depends(get_db)):
    query = text("SELECT * FROM users WHERE email = :email")
    connection = await db.get_connection()
    result = await connection.execute(query)
    await db.close_connection(connection)
    print(result.keys())
    return result

async def check_password(email,password, db: Session = Depends(get_db)):
    user = await get_user(email)
    return bcrypt.checkpw(password, user.password)

async def create_user(User):
    db = Database()
    User.password = bcrypt.hashpw(User.password, bcrypt.gensalt())
    query = text("INSERT INTO users VALUES (:User.username, :User.email, :User.firstname, :User.lastname, :User.password, :User.group, :User.profile_picture, :User.movies_watched)")
    connection = await db.get_connection()
    result = await connection.execute(query)
    await db.close_connection(connection)
    print(result.keys())
    print("User created")
    return result

