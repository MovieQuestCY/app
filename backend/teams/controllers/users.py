from moviequesttypes import User, PUser, PUserCreate
from moviequesttypes import Movie
from sqlalchemy.orm import Session

def get_user(db: Session, user_id: int) -> User:
    """Get a user by id

    Args:
        db (Session): The sqlalchemy session
        user_id (int): The id of the user

    Returns:
        User: The given user
    """
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_email(db: Session, email: str) -> User:
    """Get a user by email

    Args:
        db (Session): The sqlalchemy session
        email (str): The email of the user

    Returns:
        User: The given user
    """
    return db.query(User).filter(User.email == email).first()

def get_user_by_username(db: Session, username: str) -> User:
    """Get a user by username

    Args:
        db (Session): The sqlalchemy session
        email (str): The username of the user

    Returns:
        User: The given user
    """
    return db.query(User).filter(User.username == username).first()

def get_users(db: Session, skip: int = 0, limit: int = 100) -> list:
    """Get a list of users

    Args:
        db (Session): The sqlalchemy session
        skip (int, optional): The number of entries to skip. Defaults to 0.
        limit (int, optional): The number of entries to return. Defaults to 100.

    Returns:
        list: A list of users
    """
    return db.query(User).offset(skip).limit(limit).all()

def create_user(db: Session, user: PUserCreate) -> User:
    """Create a new user

    Args:
        db (Session): The sqlalchemy session
        user (PUserCreate): The user to create

    Returns:
        User: The created user
    """
    db_user = User(firstname=user.firstname, lastname=user.lastname, username=user.username, email=user.email, password=user.password, profile_picture=user.profile_picture, favorite_genres=user.favorite_genres)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def edit_user(db: Session, user_id: int, user: PUserCreate) -> User:
    """Edit a user

    Args:
        db (Session): The sqlalchemy session
        user_id (int): The id of the user to edit
        user (PUserEdit): The user to edit

    Returns:
        User: The edited user
    """
    db_user = db.query(User).filter(User.id == user_id).first()
    if user.firstname:
        db_user.firstname = user.firstname
    if user.lastname:
        db_user.lastname = user.lastname
    if user.username:
        db_user.username = user.username
    if user.email:
        db_user.email = user.email
    if user.password:
        db_user.password = user.password
    if user.profile_picture:
        db_user.profile_picture = user.profile_picture
    if user.favorite_genres:
        db_user.favorite_genres = user.favorite_genres
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int) -> User:
    """Delete a user

    Args:
        db (Session): The sqlalchemy session
        user_id (int): The id of the user to delete
    """
    db_user = db.query(User).filter(User.id == user_id).first()
    db.delete(db_user)
    db.commit()
    return db_user

def login_user(db: Session, email: str, password: str) -> User:
    """Login a user

    Args:
        db (Session): The sqlalchemy session
        email (str): The email of the user
        password (str): The password of the user

    Returns:
        User: The logged in user
    """
    db_user = db.query(User).filter(User.email == email).first()
    if db_user:
        if db_user.password == password:
            return db_user
    return None