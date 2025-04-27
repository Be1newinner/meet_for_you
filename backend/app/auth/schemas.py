from pydantic import BaseModel, Field, EmailStr
from datetime import datetime

class RegisterRequest(BaseModel):
    username: str = Field(..., min_length=3, max_length=30, example="vijay_dev")
    email: EmailStr = Field(..., example="vijay@example.com")
    password: str = Field(..., min_length=8, example="strongPassword123")

    class Config:
        schema_extra = {
            "example": {
                "username": "vijay_dev",
                "email": "vijay@example.com",
                "password": "strongPassword123"
            }
        }
        
class LoginRequest(BaseModel):
    email: EmailStr = Field(..., example="vijay@example.com")
    password: str = Field(..., min_length=8, example="strongPassword123")

    class Config:
        schema_extra = {
            "example": {
                "email": "vijay@example.com",
                "password": "strongPassword123"
            }
        }
        
class TokenResponse(BaseModel):
    access_token: str = Field(..., example="eyJhbGciOiJIUzI1NiIsInR5cCI6...")
    refresh_token: str = Field(..., example="dGhpcyBpcyBhIHJlZnJlc2ggdG9rZW4...")
    token_type: str = Field("bearer", example="bearer")
    expires_in: int = Field(..., description="Access token expiry in seconds", example=900)

    class Config:
        schema_extra = {
            "example": {
                "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6...",
                "refresh_token": "dGhpcyBpcyBhIHJlZnJlc2ggdG9rZW4...",
                "token_type": "bearer",
                "expires_in": 900
            }
        }
        
class UserResponse(BaseModel):
    id: str = Field(..., example="645f1e5b9c1b2c3d4e5f6789")
    username: str = Field(..., example="vijay_dev")
    email: EmailStr = Field(..., example="vijay@example.com")
    is_active: bool = Field(..., example=True)
    created_at: datetime = Field(..., example="2025-04-27T12:34:56Z")

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": "645f1e5b9c1b2c3d4e5f6789",
                "username": "vijay_dev",
                "email": "vijay@example.com",
                "is_active": True,
                "created_at": "2025-04-27T12:34:56Z"
            }
        }
        
class RefreshRequest(BaseModel):
    refresh_token: str = Field(..., example="dGhpcyBpcyBhIHJlZnJlc2ggdG9rZW4...")

    class Config:
        schema_extra = {
            "example": {
                "refresh_token": "dGhpcyBpcyBhIHJlZnJlc2ggdG9rZW4..."
            }
        }

class LogoutRequest(BaseModel):
    refresh_token: str = Field(..., example="dGhpcyBpcyBhIHJlZnJlc2ggdG9rZW4...")

    class Config:
        schema_extra = {
            "example": {
                "refresh_token": "dGhpcyBpcyBhIHJlZnJlc2ggdG9rZW4..."
            }
        }