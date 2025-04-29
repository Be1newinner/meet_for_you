from app.auth.schemas import RegisterRequest
from app.auth.models import User
from fastapi import HTTPException, status

async def register_user(register_request: RegisterRequest): 
    existing = await User.find_one(User.email == register_request.email)
    print(existing)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already exists"
        )
    user = User(
        username=register_request.username,
        email=register_request.email,
        hashed_password=register_request.password,
        full_name=register_request.full_name
    )
    await user.insert()

async def login_user(register_request: RegisterRequest): 
    resp = await User.find_one(User.email == register_request.email, projection_model={
        "_id":True,
        "email": True
    })
    print(resp)
    return resp