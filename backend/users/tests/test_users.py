import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..main import app
from ..db import Base, SessionLocal
from ..controllers.users import create_user, get_user_by_email
from moviequesttypes import PUserCreate

def get_db():
    """Get a database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a test database and a test client
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

@pytest.fixture
def client():
    app.dependency_overrides[get_db] = lambda: TestingSessionLocal()
    with TestClient(app) as test_client:
        yield test_client

# Test cases

def test_create_user_route(client):
    user = PUserCreate(email="test@example.com", password="password", username="testuser")
    response = client.post("/users/", json=user.dict())
    assert response.status_code == 200
    assert response.json()["email"] == "test@example.com"

def test_create_duplicate_user_route(client):
    user = PUserCreate(email="test@example.com", password="password", username="testuser2")
    response = client.post("/users/", json=user.dict())
    assert response.status_code == 400

def test_read_user_route(client):
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json()["email"] == "test@example.com"

def test_read_users_route(client):
    response = client.get("/users/")
    assert response.status_code == 200
    assert len(response.json()) == 1

def test_read_user_by_email_route(client):
    response = client.get("/users/by_email/test@example.com")
    assert response.status_code == 200
    assert response.json()["email"] == "test@example.com"

def test_read_user_by_username_route(client):
    response = client.get("/users/by_username/testuser")
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"

def test_delete_user_route(client):
    response = client.delete("/users/1")
    assert response.status_code == 200

def test_edit_user_route(client):
    user = PUserCreate(email="newtest@example.com", password="newpassword", username="newtestuser")
    response = client.put("/users/1", json=user.dict())
    assert response.status_code == 200
    assert response.json()["email"] == "newtest@example.com"

def test_login_user_route(client):
    user_login = {"email": "test@example.com", "password": "password"}
    response = client.post("/users/login", json=user_login)
    assert response.status_code == 200
    assert response.json()["email"] == "test@example.com"
