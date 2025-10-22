# Use official Python 3.10.5 slim image
FROM python:3.10.5-slim

# Switch to root to install system dependencies
USER root

# Install espeak-ng and clean up
RUN apt-get update && \
    apt-get install -y espeak-ng && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy your project files
COPY . .

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r backend_requirements.txt

# Set the user back to non-root (optional but recommended)
USER 1000

# Run your app
CMD ["python", "app.py"]  # Replace with your actual startup file
