from fastapi import FastAPI
from routes import movies
from db import engine
from models import sqlalchemy_schemas

sqlalchemy_schemas.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Movies API",
    description="API for movies management",
    version="0.1.0",
    contact={
        "name": "MovieQuest",
        "url": "https://moviequest.fr",
    },
)

app.include_router(movies.router)

@app.get("/")
def read_root():
    return {"Hello": "Welcome to our API"}