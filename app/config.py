
import os
from dotenv import load_dotenv

from pathlib import Path
env_path = Path(__file__).parents[1] / '.env'
load_dotenv(dotenv_path=env_path)

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    DATABASE_PORT: int = os.getenv("DATABASE_PORT")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB")
    POSTGRES_HOST: str = os.getenv("POSTGRES_HOST")
    POSTGRES_HOSTNAME: str = os.getenv("POSTGRES_HOSTNAME")

    @property
    def database_url(self) -> str:
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.DATABASE_PORT}/{self.POSTGRES_DB}"