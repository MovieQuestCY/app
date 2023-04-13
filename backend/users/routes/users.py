from typing import List
from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from ..controllers.users import create_user, get_user, get_users, get_user_by_email, get_user_by_username, delete_user, edit_user
from ..models.pydantic_schemas import User, UserCreate
from ..db import SessionLocal

user_router = APIRouter(prefix="/users")

# Dependency
def get_db():
    """Get a database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@user_router.post("/", response_model=User)
def create_user_route(user: UserCreate, db: Session = Depends(get_db)) -> User:
    """The endpoint for creating a new user

    Args:
        user (UserCreate): The user to create
        db (Session): The sqlalchemy session

    Raises:
        HTTPException: If a user with the given email already exists

    Returns:
        User: The created user
    """
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db=db, user=user)

@user_router.get("/{user_id}", response_model=User)
def read_user_route(user_id: int, db: Session = Depends(get_db)) -> User:
    """The endpoint for getting a user by id

    Args:
        user_id (int): The id of the user
        db (Session): The sqlalchemy session

    Raises:
        HTTPException: If the user does not exist

    Returns:
        User: The user with the given id
    """
    db_user = get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@user_router.get("/", response_model=List[User])
def read_users_route(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> List[User]:
    """The endpoint for getting all users

    Args:
        skip (int, optional): The number of users to skip. Defaults to 0.
        limit (int, optional): The number of users to return. Defaults to 100.
        db (Session): The sqlalchemy session

    Returns:
        List[User]: The list of users
    """
    users = get_users(db, skip=skip, limit=limit)
    return users

@user_router.get("/by_email/{email}", response_model=User)
def read_user_by_email_route(email: str, db: Session = Depends(get_db)) -> User:
    """The endpoint for getting a user by email

    Args:
        email (str): The email of the user
        db (Session): The sqlalchemy session

    Raises:
        HTTPException: If the user does not exist

    Returns:
        User: The user with the given email
    """
    db_user = get_user_by_email(db, email=email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@user_router.get("/by_username/{username}", response_model=User)
def read_user_by_username_route(username: str, db: Session = Depends(get_db)) -> User:
    """The endpoint for getting a user by username (case insensitive)

    Args:
        username (str): The username of the user
        db (Session): The sqlalchemy session

    Raises:
        HTTPException: If the user does not exist

    Returns:
        User: The user with the given username
    """
    db_user = get_user_by_username(db, username=username)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@user_router.delete("/{user_id}", response_model=User)
def delete_user_route(user_id: int, db: Session = Depends(get_db)) -> User:
    """The endpoint for deleting a user

    Args:
        user_id (int): The id of the user to delete
        db (Session): The sqlalchemy session

    Raises:
        HTTPException: If the user does not exist
    """
    db_user = get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return delete_user(db, user_id=user_id)

@user_router.put("/{user_id}", response_model=User)
def edit_user_route(user_id: int, user: UserCreate, db: Session = Depends(get_db)) -> User:
    """The endpoint for editing a user

    Args:
        user_id (int): The id of the user to edit
        user (UserCreate): The user to edit
        db (Session): The sqlalchemy session

    Raises:
        HTTPException: If the user does not exist

    Returns:
        User: The edited user
    """
    db_user = get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return edit_user(db, user_id=user_id, user=user)


