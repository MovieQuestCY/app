from pydantic import BaseModel
from typing import Union

class User(BaseModel):
    id: int
    firstname: str
    lastname: str
    username: str
    email: str
    password: str
    group: Union[str, None]
    profile_picture: Union[str, None]
    movies_watched: Union[list, None]

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    
    def add_movie(self, movie_id):
        self.movies_watched.append(movie_id) if movie_id not in self.movies_watched else None

    def remove_movie(self, movie_id):
        self.movies_watched.remove(movie_id) if movie_id in self.movies_watched else None