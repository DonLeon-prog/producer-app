from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+asyncpg://producer:producer@localhost:5432/producer"
    # REDIS_URL: str = "redis://localhost:6379"
    BOT_TOKEN: str = ""
    BOT_SECRET: str = ""
    GEMINI_API_KEY: str = ""
    JWT_SECRET: str = ""
    FRONTEND_URL: str = "http://localhost:5173"

    class Config:
        env_file = ".env"


settings = Settings()
