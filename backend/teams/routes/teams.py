from typing import List
from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from ..controllers.teams import create_team, get_team, get_teams, add_user_to_team, get_team_by_name, remove_user_from_team, delete_team, edit_team, get_users_from_team, get_teams_from_user
from moviequesttypes import PTeam, PTeamCreate, PUser
from ..db import SessionLocal

teams_router = APIRouter(prefix="/teams")

# Dependency
def get_db() -> Session:
    """Get a database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@teams_router.post("/", response_model=PTeam)
def create_team_route(team: PTeamCreate, db: Session = Depends(get_db)) -> PTeam:
    """The endpoint for creating a new team

    Args:
        team (TeamCreate): The team to create
        db (Session): The sqlalchemy session

    Raises:
        HTTPException: If a team with the given name already exists

    Returns:
        Team: The created team
    """
    db_team = get_team_by_name(db, name=team.name)
    if db_team:
        raise HTTPException(status_code=400, detail="Team with this name already exists")
    return create_team(db=db, team=team)

@teams_router.get("/{team_id}", response_model=PTeam)
def read_team_route(team_id: int, db: Session = Depends(get_db)) -> PTeam:
    """The endpoint for getting a team by id

    Args:
        team_id (int): The id of the team
        db (Session): The sqlalchemy session

    Raises:
        HTTPException: If the team does not exist

    Returns:
        Team: The team with the given id
    """
    db_team = get_team(db, team_id=team_id)
    if db_team is None:
        raise HTTPException(status_code=404, detail="Team not found")
    return db_team

@teams_router.get("/", response_model=List[PTeam])
def read_teams_route(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> List[PTeam]:
    """The endpoint for getting a list of teams

    Args:
        skip (int, optional): The number of entries to skip. Defaults to 0.
        limit (int, optional): The number of entries to return. Defaults to 100.
        db (Session): The sqlalchemy session

    Returns:
        List[Team]: A list of teams
    """
    teams = get_teams(db, skip=skip, limit=limit)
    return teams

@teams_router.post("/{team_id}/add_user/{user_id}")
def add_user_to_team_route(team_id: int, user_id: int, db: Session = Depends(get_db)) -> PUser:
    """The endpoint for adding a user to a team

    Args:
        team_id (int): The id of the team
        user_id (int): The id of the user
        db (Session): The sqlalchemy session

    Raises:
        HTTPException: If the user or team does not exist

    Returns:
        sqlalchemy.User: The user with the given id
    """
    db_team = get_team(db, team_id=team_id)
    if db_team is None:
        raise HTTPException(status_code=404, detail="Team not found")
    user = add_user_to_team(db=db, user_id=user_id, team=db_team)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
    
@teams_router.get("/by_name/{name}", response_model=PTeam)
def get_team_by_name_route(name: str, db: Session = Depends(get_db)) -> PTeam:
    """The endpoint for getting a team by name

    Args:
        name (str): The name of the team
        db (Session): The sqlalchemy session

    Raises:
        HTTPException: If the team does not exist

    Returns:
        Team: The team with the given name
    """
    db_team = get_team_by_name(db, name=name)
    if db_team is None:
        raise HTTPException(status_code=404, detail="Team not found")
    return db_team

@teams_router.delete("/{team_id}/remove_user/{user_id}")
def remove_user_from_team_route(team_id: int, user_id: int, db: Session = Depends(get_db)) -> PUser:
    """The endpoint for removing a user from a team

    Args:
        team_id (int): The id of the team
        user_id (int): The id of the user
        db (Session): The sqlalchemy session

    Raises:
        HTTPException: If the user or team does not exist

    Returns:
        sqlalchemy.User: The user with the given id
    """
    db_team = get_team(db, team_id=team_id)
    if db_team is None:
        raise HTTPException(status_code=404, detail="Team not found")
    user = remove_user_from_team(db=db, user_id=user_id, team=db_team)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@teams_router.delete("/{team_id}")
def delete_team_route(team_id: int, db: Session = Depends(get_db)) -> PTeam:
    """The endpoint for deleting a team

    Args:
        team_id (int): The id of the team
        db (Session): The sqlalchemy session

    Raises:
        HTTPException: If the team does not exist

    Returns:
        Team: The deleted team
    """
    db_team = get_team(db, team_id=team_id)
    if db_team is None:
        raise HTTPException(status_code=404, detail="Team not found")
    return delete_team(db=db, team_id=team_id)

@teams_router.put("/{team_id}")
def edit_team_route(team_id: int, edited_team: PTeamCreate, db: Session = Depends(get_db)) -> PTeam:
    """The endpoint for editing a team

    Args:
        team_id (int): The id of the team
        team (TeamCreate): The new team
        db (Session): The sqlalchemy session

    Raises:
        HTTPException: If the team does not exist OR if the team name already exists

    Returns:
        Team: The edited team
    """
    db_team = get_team(db, team_id=team_id)
    if db_team is None:
        raise HTTPException(status_code=404, detail="Team not found")
    check_team_name = get_team_by_name(db, name=edited_team.name)
    if check_team_name is not None:
        raise HTTPException(status_code=400, detail="Team with this name already exists")
    if edited_team.name is None or edited_team.name == "":
        raise HTTPException(status_code=400, detail="Team name cannot be empty")
    return edit_team(db=db, team=db_team, new_name=edited_team.name)

@teams_router.get("/{team_id}/users", response_model=List[PUser])
def get_users_in_team_route(team_id: int, db: Session = Depends(get_db)) -> List[PUser]:
    """The endpoint for getting the users in a team

    Args:
        team_id (int): The id of the team
        db (Session): The sqlalchemy session

    Raises:
        HTTPException: If the team does not exist

    Returns:
        List[User]: A list of users
    """
    db_team = get_team(db, team_id=team_id)
    if db_team is None:
        raise HTTPException(status_code=404, detail="Team not found")
    return get_users_from_team(db=db, team_id=team_id)

@teams_router.get("/{user_id}/teams", response_model=List[PTeam])
def get_teams_from_user_route(user_id: int, db: Session = Depends(get_db)) -> List[PTeam]:
    """The endpoint for getting the teams a user is in

    Args:
        user_id (int): The id of the user
        db (Session): The sqlalchemy session

    Raises:
        HTTPException: If the user does not exist

    Returns:
        List[Team]: A list of teams
    """
    return get_teams_from_user(db=db, user_id=user_id)