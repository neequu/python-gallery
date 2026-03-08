from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    auth_service_url: str = "http://localhost:8001"
    posts_service_url: str = "http://localhost:8002"
    comments_service_url: str = "http://localhost:8003"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
