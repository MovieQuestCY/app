import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .main import app
from moviequesttypes import PUserCreate
from moviequesttypes.sqlalchemy.schemas import Base
import os, tempfile
from .routes.users import get_db

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

def test_create_user_route(client):
    user = PUserCreate(email="test@example.com", password="password", username="testuser", firstname="firstname", lastname="lastname")
    response = client.post("/users/", json=user.dict())
    assert response.status_code == 200
    assert response.json()["email"] == "test@example.com"

def test_create_duplicate_user_route(client):
    user = PUserCreate(email="test@example.com", password="password", username="testuser2", firstname="firstname", lastname="lastname")
    response = client.post("/users/", json=user.dict())
    assert response.status_code == 409

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

def test_login_user_route(client):
    user_login = {"email": "test@example.com", "password": "password"}
    response = client.post("/users/login", json=user_login)
    assert response.status_code == 200
    assert response.json()["email"] == "test@example.com"

def test_edit_user_route(client):
    user = PUserCreate(email="test@example.com", password="newpassword", username="newtestuser", firstname="firstname", lastname="lastname")
    response = client.put("/users/1", json=user.dict())
    assert response.status_code == 200
    assert response.json()["username"] == "newtestuser"

def test_delete_user_route(client):
    response = client.delete("/users/1")
    assert response.status_code == 200