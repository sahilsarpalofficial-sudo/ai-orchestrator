from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "AgentOS"
    database_url: str | None = None

    class Config:
        env_file = ".env"


settings = Settings()

