from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from .database import DBUser, SessionLocal
import os

import sys
sys.path.append('.')
sys.path.append('../')
sys.path.append('../app/')
sys.path.append('./models')

from .models.user import User


app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def get_home():
    html_path = os.path.join(os.path.dirname(__file__), "html/home.html")
    with open(html_path, "r") as file:
        return file.read()

# Endpoint to get users
@app.get("/users/", response_model=list[User])
def get_users():
    try:
        session = SessionLocal()
        users = session.query(DBUser).all()
        session.close()
        # Convert each DBUser object to a dictionary using the to_dict() method
        user_dicts = [user.to_dict() for user in users]
    except Exception as e:
        return {"message": "Error getting users" + str(e)}
    return user_dicts

# Endpoint to save a new user
@app.post("/users/", status_code=201)
def save_user(user: User):
    try:
        db_user = DBUser(name=user.name, email=user.email, company=user.company, title=user.title) # Create a DBUser object from the User model
        print(db_user.to_dict())
        session = SessionLocal()
        session.add(db_user)
        session.commit()
        session.close()
    except Exception as e:
        return {"message": "Error saving user" + str(e)}

    return {"message": "User created successfully"}

