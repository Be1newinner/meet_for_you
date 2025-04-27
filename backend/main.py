from fastapi import FastAPI
# from app.core.config import settings
from app.auth.routers import auth_router

app = FastAPI()

@app.get("/")
def welcome_msg():
    return {
        "message": "Welcome to Meet for You"
    }

app.include_router(auth_router, prefix="/auth", tags=["Authentication"])