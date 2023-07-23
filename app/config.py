
import os
from dotenv import load_dotenv

from pathlib import Path
env_path = Path(__file__).parents[1] / '.env'
load_dotenv(dotenv_path=env_path)

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL")

    @property
    def database_url(self) -> str:
        return self.DATABASE_URL