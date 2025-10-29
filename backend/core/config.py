from pydantic import BaseSettings

class Settings(BaseSettings):
    OPENAI_API_KEY: str | None = None
    CALENDLY_API_KEY: str | None = None
    TIMEZONE: str = 'Asia/Kolkata'
    BACKEND_PORT: int = 8000

    class Config:
        env_file = '.env'

settings = Settings()
