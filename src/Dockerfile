# Use official Python image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy files
COPY app.py requirements.txt ./

# Install dependencies
RUN pip install -r requirements.txt

# Expose ports
EXPOSE 5000 8000

# Start the application
CMD ["python", "app.py"]

