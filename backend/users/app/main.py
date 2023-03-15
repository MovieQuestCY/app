from fastapi import FastAPI
from routes import users, teams
from db import engine
from models import sqlalchemy_schemas

sqlalchemy_schemas.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Users API",
    description="API for users management",
    version="0.1.0",
    contact={
        "name": "MovieQuest",
        "url": "https://moviequest.fr",
    },
)

app.include_router(users.user_router)
app.include_router(teams.teams_router)

@app.get("/")
def read_root():
    return {"Hello": "Welcome to our API"}
