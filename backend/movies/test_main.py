import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .main import app
from moviequesttypes.sqlalchemy.schemas import Base
from moviequesttypes.pydantic.Movie import PMovieCreate
import os, tempfile
from .routes.movies import get_db

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


# Test creating a new movie
def test_create_movie(client):
    new_movie = PMovieCreate(id=1, title="Test Movie", overview="", release_date="", genres="", vote_average=0.0, popularity=0, poster_path="")
    response = client.post("/movies/", json=new_movie.dict())
    assert response.status_code == 200
    assert response.json()["title"] == "Test Movie"

# Test getting a movie by id
def test_read_movie(client):
    movie_id = 1
    response = client.get(f"/movies/{movie_id}")
    assert response.status_code == 200
    assert response.json()["id"] == movie_id

# Test getting a list of movies
def test_read_movies(client):
    response = client.get("/movies/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# Test getting a movie by title
def test_read_movie_by_title(client):
    movie_title = "Test Movie"
    response = client.get(f"/movies/by_title/{movie_title}")
    assert response.status_code == 200
    assert response.json()["title"] == movie_title

# Test editing a movie
def test_edit_movie(client):
    movie_id = 1
    edited_movie = PMovieCreate(id=1, title="Updated title Test Movie", overview="", release_date="", genres="", vote_average=0.0, popularity=0, poster_path="")
    response = client.put(f"/movies/{movie_id}", json=edited_movie)
    assert response.status_code == 200
    assert response.json()["title"] == edited_movie["title"]

# Test deleting a movie
def test_delete_movie(client):
    movie_id = 2
    response = client.delete(f"/movies/{movie_id}")
    assert response.status_code == 200
    assert response.json()["id"] == movie_id