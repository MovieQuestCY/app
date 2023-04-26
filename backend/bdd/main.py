from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .db import engine
from .schemas.sqlalchemy import schemas

schemas.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="BDD Builder API",
    description="API for building BDD",
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

@app.get("/")
def build_bdd():
    return {'200': 'OK'}
