from moviequesttypes import PMovie, PMovieCreate
from moviequesttypes import Movie
from sqlalchemy.orm import Session

def get_movies(db: Session, skip=int, limit=int) -> Movie:
    return db.query(Movie).offset(skip).limit(limit).all()

def get_movie(db: Session, movie_id: int) -> Movie:
    return db.query(Movie).filter(Movie.id == movie_id).first()

def get_movie_by_title(db: Session, title: str) -> Movie:
    return db.query(Movie).filter(Movie.title == title).first()

def create_movie(db: Session, movie: PMovieCreate) -> Movie:
    db_movie = Movie(
        id=movie.id,
        title=movie.title,
        overview=movie.overview,
        release_date=movie.release_date,
        genres=movie.genres,
        vote_average=movie.vote_average,
        popularity=movie.popularity,
        poster_path=movie.poster_path
    )
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie

def edit_movie(db: Session, movie: PMovie, movie_id: int) -> Movie:
    db_movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if movie.title:
        db_movie.title = movie.title
    if movie.overview:
        db_movie.overview = movie.overview
    if movie.release_date:
        db_movie.release_date = movie.release_date
    if movie.genres:
        db_movie.genres = movie.genres
    if movie.vote_average:
        db_movie.vote_average = movie.vote_average
    if movie.popularity:
        db_movie.popularity = movie.popularity
    if movie.poster_path:
        db_movie.poster_path = movie.poster_path
    db.commit()
    db.refresh(db_movie)
    return db_movie

def delete_movie(db: Session, movie_id: int) -> Movie:
    db_movie = db.query(Movie).filter(Movie.id == movie_id).first()
    db.delete(db_movie)
    db.commit()
    return db_movie