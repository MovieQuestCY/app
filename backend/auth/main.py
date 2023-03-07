from fastapi import FastAPI
import uvicorn
from sqlalchemy import create_engine

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("backend/auth/connect/{email}")
async def connectUser(email: str, password: str):
    if(password != "password"):
        return {"message": "Invalid password"}
    else:
        return {"message": f"Welcome {email}"}

@app.get("backend/auth/newUser/{email}")
async def newUser(email: str, password: str):
    #insert into database
    return {"message": f"Welcome {email}"}

engine = create_engine("mysql+pymysql://root:p4ssw0rd@db.neuvy.eu:3306?charset=utf8mb4")

if __name__ == "__main__":
    config = uvicorn.Config("main:app", port=5000, log_level="info")
    server = uvicorn.Server(config)
    server.run()
