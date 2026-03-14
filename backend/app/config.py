import os

from dotenv import load_dotenv
from pydantic import BaseSettings


load_dotenv()


class Settings(BaseSettings):
    app_name: str = "AgentOS"
    database_url: str | None = None
    openai_api_key: str | None = os.getenv("OPENAI_API_KEY")

    class Config:
        env_file = ".env"


settings = Settings()
