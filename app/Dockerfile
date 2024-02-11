# Use the official Python base image
FROM python:3.10-slim-bookworm

# Set the working directory in the container
WORKDIR /

# Copy the application code to the working directory
COPY . /app/.

# Install the dependencies
RUN pip install -r app/requirements.txt

# Start the FastAPI application
CMD ["uvicorn", "--host", "0.0.0.0", "--port", "5000", "app.main:app"]
