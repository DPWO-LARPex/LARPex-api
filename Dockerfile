# Use official Python 3.11 image as base
FROM python:3.11

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# # Set working directory
WORKDIR /larpex-api

# Install system dependencies
RUN apt-get update

# Install Python dependencies
COPY requirements.txt /larpex-api/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy FastAPI application into the container
COPY app/ /larpex-api/

# Expose port
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
