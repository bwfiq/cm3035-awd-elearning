# Stage 1: Base build stage
FROM python:3-slim
 
# Create the app directory
RUN mkdir /app
 
# Set the working directory
WORKDIR /app
 
# Upgrade pip and install dependencies
RUN pip install --upgrade pip 
 
# Copy the requirements file first (better caching)
COPY . .
 
# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt
 
# Expose the application port
EXPOSE 8000 
 
# Start the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]