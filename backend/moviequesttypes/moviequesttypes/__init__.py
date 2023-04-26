from .pydantic.Movie import Movie, MovieCreate, MovieBase
from .pydantic.User import User, UserCreate, UserBase, UserLogin, UserLogged
from .pydantic.Team import Team, TeamCreate, TeamBase
from .sqlalchemy.schemas import Movie, User, Team, has_team, has_watched