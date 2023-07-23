from pydantic import BaseModel

# Pydantic model for the User
class User(BaseModel):
    name: str
    email: str
    company: str