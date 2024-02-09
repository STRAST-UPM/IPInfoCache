# Use the official Python base image
FROM python:3.10-slim-bookworm

# Set the working directory in the container
WORKDIR /

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the application code to the working directory
COPY . /app/.

# Start the FastAPI application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]
