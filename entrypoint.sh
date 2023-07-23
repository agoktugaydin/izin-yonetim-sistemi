#!/bin/bash

# Apply the Alembic migrations
alembic upgrade head

# Start the FastAPI application using uvicorn
uvicorn app.main:app --host 0.0.0.0 --port 8000
