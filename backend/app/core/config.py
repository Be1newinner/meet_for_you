from pydantic import AnyUrl, Field
from pydantic_settings import BaseSettings
 
class Settings(BaseSettings):
    # ─── App Metadata ──────────────────────────────────────────────
    APP_NAME: str = "SocialMediaApp"
    DEBUG: bool = Field(default=False, env="DEBUG")

    # ─── MongoDB ────────────────────────────────────────────────────
    MONGODB_URI: AnyUrl = Field(..., env="MONGODB_URI")  

    # ─── JWT / Auth ────────────────────────────────────────────────
    SECRET_KEY: str = Field(..., env="SECRET_KEY")  
    ALGORITHM: str = Field(default="HS256", env="ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(default=15, env="ACCESS_TOKEN_EXPIRE_MINUTES")
    REFRESH_TOKEN_EXPIRE_DAYS: int = Field(default=7, env="REFRESH_TOKEN_EXPIRE_DAYS")

    # ─── CORS / Security ────────────────────────────────────────────
    # BACKEND_CORS_ORIGINS: list[str] = Field(
    #     default='["http://localhost", "http://localhost:3000"]',
    #     env="BACKEND_CORS_ORIGINS"
    # )

    # ─── Cloud Storage (Optional) ───────────────────────────────────
    CLOUDINARY_CLOUD_NAME: str = Field(default="", env="CLOUDINARY_CLOUD_NAME")
    CLOUDINARY_API_KEY: str = Field(default="", env="CLOUDINARY_API_KEY")
    CLOUDINARY_API_SECRET: str = Field(default="", env="CLOUDINARY_API_SECRET")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True

settings = Settings()