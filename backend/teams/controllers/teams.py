from moviequesttypes import Team, User, PTeam, PTeamCreate, PUser
from sqlalchemy.orm import Session

def get_team(db: Session, team_id: int) -> Team:
    """Get a team by id

    Args:
        db (Session): The sqlalchemy session
        team_id (int): The id of the team

    Returns:
        Team: The team with the given id
    """
    return db.query(Team).filter(Team.id == team_id).first()

def get_teams(db: Session, skip: int = 0, limit: int = 100) -> list:
    """Get a list of teams

    Args:
        db (Session): The sqlalchemy session
        skip (int, optional): The number of entries to skip. Defaults to 0.
        limit (int, optional): The number of entries to return. Defaults to 100.

    Returns:
        list: A list of teams
    """
    return db.query(Team).offset(skip).limit(limit).all()

def get_team_by_name(db: Session, name: str) -> Team:
    """Get a team by name

    Args:
        db (Session): The sqlalchemy session
        name (str): The name of the team

    Returns:
        Team: The team with the given name
    """
    return db.query(Team).filter(Team.name == name).first()

def create_team(db: Session, team: PTeamCreate) -> Team:
    """Create a new team

    Args:
        db (Session): The sqlalchemy session
        team (PTeamCreate): The team to create

    Returns:
        Team: The created team
    """
    db_team = Team(name=team.name)
    db.add(db_team)
    db.commit()
    db.refresh(db_team)
    return db_team

def add_user_to_team(db: Session, user: User, team: Team) -> User:
    """Add a user to a team

    Args:
        db (Session): The sqlalchemy session
        user_id (int): The id of the user
        team_id (int): The id of the team

    Returns:
        User: The user with the added team
    """
    user.teams.append(team)
    db.commit()
    db.refresh(user)
    return user

def remove_user_from_team(db: Session, user: PUser, team: PTeam) -> User:
    """Remove a user from a team

    Args:
        db (Session): The sqlalchemy session
        user_id (int): The id of the user to delete
        team_id (int): The id of the team where the user is deleted

    Returns:
        User: The removed user
    """
    db_user = user
    db_team = team
    db_user.teams.remove(db_team)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_team(db: Session, team_id: int) -> Team:
    """Delete a team

    Args:
        db (Session): The sqlalchemy session
        team_id (int): The id of the team to delete

    Returns:
        Team: The deleted team
    """
    db_team = get_team(db, team_id=team_id)
    db.delete(db_team)
    db.commit()
    return db_team

def edit_team(db: Session, team: PTeam, new_name:str) -> Team:
    """Edit a team

    Args:
        db (Session): The sqlalchemy session
        team_id (int): The id of the team to edit
        team (PTeamCreate): The new team

    Returns:
        Team: The edited team
    """
    team.name = new_name
    db.commit()
    db.refresh(team)
    return team

def get_users_from_team(db: Session, team_id: int) -> list:
    """Get a list of users from a team

    Args:
        db (Session): The sqlalchemy session
        team_id (int): The id of the team

    Returns:
        list: A list of users
    """
    #db_team = get_team(db, team_id=team_id)
    return db.query(User).filter(User.teams.any(id=team_id)).all()