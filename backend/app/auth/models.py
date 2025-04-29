from datetime import datetime
from typing import Optional, Annotated

from beanie import Document, Indexed
from pydantic import EmailStr, Field

class User(Document):
    username: Annotated[str, Indexed(unique=True)] = Field(..., min_length=3, max_length=30)
    email: Annotated[EmailStr, Indexed(unique=True)] = Field(...) 
    hashed_password: str = Field(..., min_length=5, max_length=128)
    is_active: bool = Field(default=True)
        
    full_name: Optional[str] = Field(None, max_length=100)
    bio: Optional[str] = Field(None, max_length=280)
    avatar_url: Optional[str] = Field(None, example="https://cdn.example.com/avatars/uid.jpg")

    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    
    class Settings:
        name = "users"
        
    class Config:
        schema_extra = {
            "example": {
                "username": "vijay_dev",
                "email": "vijay@example.com",
                "hashed_password": "$2b$12$KIX5...",
                "is_active": True,
                "full_name": "Vijay Kumar",
                "bio": "Full Stack Dev | FAANG Aspirant",
                "avatar_url": "https://cdn.example.com/avatars/645f1e5b9c1b2c3d4e5f6789.jpg",
                "created_at": "2025-04-27T12:34:56Z",
                "updated_at": "2025-04-27T12:34:56Z"
            }
        }
