from ..models import sqlalchemy_schemas, pydantic_schemas
from sqlalchemy.orm import Session

def get_movies(db: Session, skip=int, limit=int) -> sqlalchemy_schemas.Movie:
    return db.query(sqlalchemy_schemas.Movie).offset(skip).limit(limit).all()

def get_movie(db: Session, movie_id: int) -> sqlalchemy_schemas.Movie:
    return db.query(sqlalchemy_schemas.Movie).filter(sqlalchemy_schemas.Movie.id == movie_id).first()

def get_movie_by_title(db: Session, title: str) -> sqlalchemy_schemas.Movie:
    return db.query(sqlalchemy_schemas.Movie).filter(sqlalchemy_schemas.Movie.title == title).first()

def create_movie(db: Session, movie: pydantic_schemas.MovieCreate) -> sqlalchemy_schemas.Movie:
    db_movie = sqlalchemy_schemas.Movie(
        title=movie.title,
        description=movie.description,
        year=movie.year,
        director=movie.director,
        genre=movie.genre,
    )
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie

def edit_movie(db: Session, movie: pydantic_schemas.Movie, movie_id: int) -> sqlalchemy_schemas.Movie:
    db_movie = db.query(sqlalchemy_schemas.Movie).filter(sqlalchemy_schemas.Movie.id == movie_id).first()
    if movie.title:
        db_movie.title = movie.title
    if movie.year:
        db_movie.year = movie.year
    if movie.genre:
        db_movie.genre = movie.genre
    if movie.director:
        db_movie.director = movie.director
    db.commit()
    db.refresh(db_movie)
    return db_movie

def delete_movie(db: Session, movie_id: int) -> sqlalchemy_schemas.Movie:
    db_movie = db.query(sqlalchemy_schemas.Movie).filter(sqlalchemy_schemas.Movie.id == movie_id).first()
    db.delete(db_movie)
    db.commit()
    return db_movie