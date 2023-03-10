from fastapi import FastAPI
import uvicorn
from routes import auth

app = FastAPI()

app.include_router(auth.router)

if __name__ == "__main__":
    config = uvicorn.Config("main:app", port=5000, log_level="info")
    server = uvicorn.Server(config)
    server.run()
