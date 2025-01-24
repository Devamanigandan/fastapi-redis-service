from fastapi import FastAPI
import uvicorn

from app.routers import users

app = FastAPI()

app.include_router(users.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9001)