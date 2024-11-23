from fastapi import FastAPI, Request, status
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from .database import DBUser, SessionLocal

# from .database import SessionLocal, engine
import os

import sys

sys.path.append(".")
sys.path.append("../")
sys.path.append("../app/")
sys.path.append("./models")

from .models.user import User

import ptvsd

# Enable ptvsd remote debugging
ptvsd.enable_attach(address=("localhost", 5678))

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def get_home(request: Request):
    title = "İzin Yönetim Uygulaması"
    description = "Bu uygulama çalışanların izin talep edebilmesini ve yetkililerin izinleri yönetebilmesini sağlar."
    return templates.TemplateResponse(
        "home.html",
        {
            "request": request,
            "title": title,
            "description": description,
        },
    )


# Endpoint to get users
@app.get("/users/", response_class=HTMLResponse)
async def get_users(request: Request):
    try:
        session = SessionLocal()
        users = session.query(DBUser).all()
        session.close()
        # Convert each DBUser object to a dictionary using the to_dict() method
        user_dicts = [user.to_dict() for user in users]
    except Exception as e:
        error = "Error getting users" + str(e)
        return templates.TemplateResponse(
            "error.html",
            {"request": request, "error": error},
            status_code=status.HTTP_400_BAD_REQUEST,
        )
    return templates.TemplateResponse(
        "user_list.html", {"request": request, "users": user_dicts}
    )


# Endpoint to save a new user
@app.post("/users/", response_class=HTMLResponse)
async def save_user(request: Request):
    try:
        user_json = await request.json()
        # Extract the user data from the JSON request
        name = user_json["name"]
        email = user_json["email"]
        company = user_json["company"]
        title = user_json["title"]
        # Create a User object from the extracted user data
        user = User(name=name, email=email, company=company, title=title)

        # Create a DBUser object from the User object
        db_user = DBUser(
            name=user.name, email=user.email, company=user.company, title=user.title
        )

        session = SessionLocal()
        session.add(db_user)
        session.commit()
        session.close()
    except Exception as e:
        error = "Error creating user" + str(e)
        return templates.TemplateResponse(
            "error.html",
            {"request": request, "error": error},
            status_code=status.HTTP_400_BAD_REQUEST,
        )
    return RedirectResponse(url="/users", status_code=status.HTTP_303_SEE_OTHER)


# Endpoint to get a user by email
@app.get("/users/{email}", response_class=HTMLResponse)
async def get_user(request: Request, email: str):
    try:
        session = SessionLocal()
        db_user = session.query(DBUser).filter(DBUser.email == email).first()
        session.close()
        # Create a User object from the DBUser object
        user = User(
            name=db_user.name,
            email=db_user.email,
            company=db_user.company,
            title=db_user.title,
        )
    except Exception as e:
        error = "Error getting user" + str(e)
        return templates.TemplateResponse(
            "error.html",
            {"request": request, "error": error},
            status_code=status.HTTP_400_BAD_REQUEST,
        )
    return templates.TemplateResponse("user.html", {"request": request, "user": user})
