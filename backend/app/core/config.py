from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    # Database
    DATABASE_URL: str = "sqlite:///./grocery_tracker.db"
    
    # CORS
    CORS_ORIGINS: list[str] = ["http://localhost:8081", "http://localhost:19006", "exp://localhost:8081"]
    
    # OCR
    TESSERACT_CMD: Optional[str] = None  # Will use system default if not set
    
    # Notification
    NOTIFICATION_DAYS_BEFORE_EXPIRY: int = 2
    
    # Expiry Prediction
    DEFAULT_EXPIRY_DAYS: int = 7  # Default expiry for items without specific prediction
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()

