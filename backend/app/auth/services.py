from app.auth.schemas import RegisterRequest
from app.auth.models import User
from fastapi import HTTPException, status
from pydantic import BaseModel
from beanie import Document
from typing import Type

from app.auth.utils import hashing

async def is_doc_exists(model: Type[Document], query: dict) -> bool:
    doc = await model.find_one(query, projection={"_id": 1})
    return doc is not None

async def register_user(register_request: RegisterRequest): 
    if not is_doc_exists(User, {"email": register_request.email }):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already exists"
        )
    hashed_password = hashing(register_request.password)
    user = User(
        username=register_request.username,
        email=register_request.email,
        password=hashed_password,
        full_name=register_request.full_name
    )
    data = await user.insert()
    return data


async def login_user(register_request: RegisterRequest): 
    resp = await User.find_one(User.email == register_request.email, projection_model={"password": 1})
    return resp