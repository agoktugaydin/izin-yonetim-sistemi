# Use the official Python image as the base image
FROM python:3.9-slim

# Install PostgreSQL development package inside the container
RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2
# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Copy the alembic folder into the container
COPY alembic alembic

# Copy the alembic.ini file into the container
COPY alembic.ini .

# Copy the entrypoint.sh script into the container
COPY entrypoint.sh .

# Copy the .env script into the container
COPY .env .env

# Copy the entire app directory into the container
COPY app app

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Make the entrypoint script executable
RUN chmod +x entrypoint.sh

# Set the entrypoint for the container
ENTRYPOINT ["./entrypoint.sh"]