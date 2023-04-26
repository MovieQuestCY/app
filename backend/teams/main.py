from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import teams

app = FastAPI(
    title="teams API",
    description="API for users management",
    version="0.1.0",
    contact={
        "name": "MovieQuest",
        "url": "https://moviequest.fr",
    },
)

origins = [
    "*"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(teams.teams_router)

@app.get("/")
def read_root():
    return {"Hello": "Welcome to our API"}