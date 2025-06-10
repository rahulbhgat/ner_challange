# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy entire app
COPY . .

# Expose port 7860 (Hugging Face Spaces expects 7860)
EXPOSE 7860

# Command to run the app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]
