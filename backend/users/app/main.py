from fastapi import FastAPI
from routes import users

app = FastAPI(
    title="Users API",
    description="API for users management",
    version="0.1.0",
    contact={
        "name": "MovieQuest",
        "url": "https://moviequest.fr",
    },
)

app.include_router(users.router)
