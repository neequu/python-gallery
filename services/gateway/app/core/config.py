from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    auth_service_url: str = "http://localhost:8001"
    posts_service_url: str = "http://localhost:8002"

    class Config:
        env_file = ".env"


settings = Settings()