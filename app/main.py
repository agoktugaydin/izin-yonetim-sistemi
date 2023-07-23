from fastapi import FastAPI, HTTPException

from .database import DBUser, SessionLocal

import sys
sys.path.append('.')
sys.path.append('../')
sys.path.append('../app/')
sys.path.append('./models')

from .models.user import User


app = FastAPI()

# Endpoint to get users
@app.get("/users/", response_model=list[User])
def get_users():
    session = SessionLocal()
    users = session.query(DBUser).all()
    session.close()
    # Convert each DBUser object to a dictionary using the to_dict() method
    user_dicts = [user.to_dict() for user in users]
    return user_dicts

# Endpoint to save a new user
@app.post("/users/", status_code=201)
def save_user(user: User):
    db_user = DBUser(name=user.name, email=user.email)
    session = SessionLocal()
    session.add(db_user)
    session.commit()
    session.close()
    return {"message": "User created successfully"}
