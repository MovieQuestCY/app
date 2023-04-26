from ..models import sqlalchemy_schemas, pydantic_schemas
from sqlalchemy.orm import Session
import jwt
from datetime import datetime, timedelta

def get_user(db: Session, user_id: int) -> sqlalchemy_schemas.User:
    """Get a user by id

    Args:
        db (Session): The sqlalchemy session
        user_id (int): The id of the user

    Returns:
        sqlalchemy_schemas.User: The given user
    """
    return db.query(sqlalchemy_schemas.User).filter(sqlalchemy_schemas.User.id == user_id).first()

def get_user_by_email(db: Session, email: str) -> sqlalchemy_schemas.User:
    """Get a user by email

    Args:
        db (Session): The sqlalchemy session
        email (str): The email of the user

    Returns:
        sqlalchemy_schemas.User: The given user
    """
    return db.query(sqlalchemy_schemas.User).filter(sqlalchemy_schemas.User.email == email).first()

def get_user_by_username(db: Session, username: str) -> sqlalchemy_schemas.User:
    """Get a user by username

    Args:
        db (Session): The sqlalchemy session
        email (str): The username of the user

    Returns:
        sqlalchemy_schemas.User: The given user
    """
    return db.query(sqlalchemy_schemas.User).filter(sqlalchemy_schemas.User.username == username).first()

def get_users(db: Session, skip: int = 0, limit: int = 100) -> list:
    """Get a list of users

    Args:
        db (Session): The sqlalchemy session
        skip (int, optional): The number of entries to skip. Defaults to 0.
        limit (int, optional): The number of entries to return. Defaults to 100.

    Returns:
        list: A list of users
    """
    return db.query(sqlalchemy_schemas.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: pydantic_schemas.UserCreate) -> sqlalchemy_schemas.User:
    """Create a new user

    Args:
        db (Session): The sqlalchemy session
        user (pydantic_schemas.UserCreate): The user to create

    Returns:
        sqlalchemy_schemas.User: The created user
    """
    hashed_password = user.password + "notreallyhashed" #TODO: actually hash the password
    db_user = sqlalchemy_schemas.User(firstname=user.firstname, lastname=user.lastname, username=user.username, email=user.email, password=hashed_password, profile_picture=user.profile_picture, favorite_genres=user.favorite_genres)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def edit_user(db: Session, user_id: int, user: pydantic_schemas.UserCreate) -> sqlalchemy_schemas.User:
    """Edit a user

    Args:
        db (Session): The sqlalchemy session
        user_id (int): The id of the user to edit
        user (pydantic_schemas.UserEdit): The user to edit

    Returns:
        sqlalchemy_schemas.User: The edited user
    """
    db_user = db.query(sqlalchemy_schemas.User).filter(sqlalchemy_schemas.User.id == user_id).first()
    if user.firstname:
        db_user.firstname = user.firstname
    if user.lastname:
        db_user.lastname = user.lastname
    if user.username:
        db_user.username = user.username
    if user.email:
        db_user.email = user.email
    if user.password:
        db_user.password = user.password + "notreallyhashed" #TODO: actually hash the password
    if user.profile_picture:
        db_user.profile_picture = user.profile_picture
    if user.favorite_genres:
        db_user.favorite_genres = user.favorite_genres
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int) -> sqlalchemy_schemas.User:
    """Delete a user

    Args:
        db (Session): The sqlalchemy session
        user_id (int): The id of the user to delete
    """
    db_user = db.query(sqlalchemy_schemas.User).filter(sqlalchemy_schemas.User.id == user_id).first()
    db.delete(db_user)
    db.commit()
    return db_user

def create_jwt_token(secret: str, algorithm: str, user: sqlalchemy_schemas.User) -> str:
    """Create a jwt token

    Args:
        secret (str): The secret to use
        algorithm (str): The algorithm to use
        user (sqlalchemy_schemas.User): The user to create the token for

    Returns:
        str: The jwt token
    """
    
    expiration = datetime.utcnow() + timedelta(days=14)
    to_encode = {"exp": expiration, "sub": str(user.id)}
    encoded_jwt = jwt.encode(to_encode, secret, algorithm=algorithm)
    return encoded_jwt

def login_user(db: Session, email: str, password: str) -> sqlalchemy_schemas.User:
    """Login a user

    Args:
        db (Session): The sqlalchemy session
        email (str): The email of the user
        password (str): The password of the user

    Returns:
        sqlalchemy_schemas.User: The logged in user
    """
    db_user = db.query(sqlalchemy_schemas.User).filter(sqlalchemy_schemas.User.email == email).first()
    if db_user:
        if db_user.password == password + "notreallyhashed": #TODO: actually hash the password
            return db_user
    return None
