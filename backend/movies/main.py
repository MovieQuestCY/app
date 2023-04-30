from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import movies

app = FastAPI(
    title="Movie API",
    description="API for movies management",
    version="0.1.0",
    contact={
        "name": "MovieQuest",
        "url": "https://moviequest.fr",
    },
)

origins = [
    "http://front.dev.neuvy.eu",
    "https://moviequest.neuvy.eu"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(movies.movie_router)

@app.get("/")
def read_root():
    return {"Hello": "Welcome to our API"}
