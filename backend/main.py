from fastapi import FastAPI
from contextlib import asynccontextmanager
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from app.auth.routers import auth_router
from shared.core.config import settings

# Models
from app.auth.models import User

@asynccontextmanager
async def lifespan(_app: FastAPI):
    client = AsyncIOMotorClient(str(settings.MONGODB_URI))
    await init_beanie(database=client.get_default_database(), document_models=[User])
    yield
    client.close()

app = FastAPI(debug=True, lifespan=lifespan)
    
@app.get("/")
def welcome_msg():
    return {
        "message": "Welcome to Meet for You"
    }

app.include_router(auth_router, prefix="/auth", tags=["Authentication"])