from fastapi import FastAPI
from routes import auth

app = FastAPI(
    title="Auth API",
    description="API for auth management",
    version="0.1.0",
    contact={
        "name": "MovieQuest",
        "url": "https://moviequest.fr",
    },
)

app.include_router(auth.router)
