from moviequesttypes.pydantic.User import PUserCreate
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .main import app
from moviequesttypes.sqlalchemy.schemas import Base
import os, tempfile
from .routes.teams import get_db

@pytest.fixture(scope="function")
def client():
    db_fd, db_path = tempfile.mkstemp()
    engine = create_engine(f"sqlite:///{{db_path}}")
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)
    Base.metadata.create_all(bind=engine)
    def get_test_db():
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()
    app.dependency_overrides[get_db] = get_test_db
    with TestClient(app) as test_client:
        yield test_client
    os.close(db_fd)
    os.unlink


# Test cases

def test_create_team(client):
    new_team = {"name": "Test Team"}
    response = client.post("/teams/", json=new_team)
    assert response.status_code == 200
    assert response.json()["name"] == new_team["name"]

# Test getting a team by id
def test_read_team(client):
    team_id = 1
    response = client.get(f"/teams/{team_id}")
    assert response.status_code == 200
    assert response.json()["id"] == team_id

# Test getting a list of teams
def test_read_teams(client):
    response = client.get("/teams/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# Test getting a team by name
def test_get_team_by_name(client):
    team_name = "Test Team"
    response = client.get(f"/teams/by_name/{team_name}")
    assert response.status_code == 200
    assert response.json()["name"] == team_name


# Test getting users in a team
def test_get_users_in_team(client):
    team_id = 1
    response = client.get(f"/teams/{team_id}/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# Test editing a team
def test_edit_team(client):
    team_id = 1
    edited_team = {"name": "Updated Test Team"}
    response = client.put(f"/teams/{team_id}", json=edited_team)
    assert response.status_code == 200
    assert response.json()["name"] == edited_team["name"]

# Test deleting a team
def test_delete_team(client):
    team_id = 1
    response = client.delete(f"/teams/{team_id}")
    assert response.status_code == 200
    assert response.json()["id"] == team_id