from fastapi import APIRouter
from app.auth.schemas import RegisterRequest, LoginRequest
from app.auth.services import register_user, login_user

auth_router = APIRouter()

@auth_router.post("/register")
async def register(register_request: RegisterRequest):
    return await register_user(register_request)

@auth_router.post("/login")
async def login(login_request: LoginRequest):
    return await login_user(login_request)