from typing import List
from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from ..controllers.movies import create_movie, get_movie, get_movies, get_movie_by_title, delete_movie, edit_movie
from moviequesttypes import PMovie, PMovieCreate
from ..db import SessionLocal

movie_router = APIRouter(prefix="/movies")

# Dependency
def get_db():
    """Get a database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#TODO : Find another point to check if the movie already exists
@movie_router.post("/", response_model=PMovie)
def create_movie_route(movie: PMovieCreate, db: Session = Depends(get_db)) -> PMovie:
    db_movie = get_movie_by_title(db, title=PMovie.title)
    if db_movie:
        raise HTTPException(status_code=400, detail="Title already registered")
    return create_movie(db=db, movie=PMovie)

@movie_router.get("/{movie_id}", response_model=PMovie)
def read_movie_route(movie_id: int, db: Session = Depends(get_db)) -> PMovie:
    db_movie = get_movie(db, movie_id=movie_id)
    if db_movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return db_movie

@movie_router.get("/", response_model=List[PMovie])
def read_movies_route(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> List[PMovie]:
    movies = get_movies(db, skip=skip, limit=limit)
    return movies

@movie_router.get("/by_title/{title}", response_model=PMovie)
def read_movie_by_title_route(title: str, db: Session = Depends(get_db)) -> PMovie:
    db_movie = get_movie_by_title(db, title=title)
    if db_movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return db_movie

@movie_router.delete("/{movie_id}", response_model=PMovie)
def delete_movie_route(movie_id: int, db: Session = Depends(get_db)) -> PMovie:
    db_movie = get_movie(db, movie_id=movie_id)
    if db_movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return delete_movie(db, movie_id=movie_id)

@movie_router.put("/{movie_id}", response_model=PMovie)
def edit_movie_route(movie_id: int, movie: PMovieCreate, db: Session = Depends(get_db)) -> PMovie:
    db_movie = get_movie(db, movie_id=movie_id)
    if db_movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return edit_movie(db, movie_id=movie_id, movie=movie)



