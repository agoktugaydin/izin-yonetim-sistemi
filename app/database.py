from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import sys
sys.path.append('.')
sys.path.append('../')
sys.path.append('../app/')

from .config import Settings

settings = Settings()
SQLALCHEMY_DATABASE_URL = settings.database_url

# SQLAlchemy setup
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# # Create the tables when the app starts
# Base.metadata.create_all(bind=engine)

# SQLAlchemy model for the User table


class DBUser(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, index=True)
    email = Column(String, index=True)
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email
            # Add other attributes if needed
        }
