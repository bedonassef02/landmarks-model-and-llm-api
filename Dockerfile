# Use a base image with Python pre-installed
FROM python:3.11.5

# Set the working directory
WORKDIR /app

# Copy the requirements.txt file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files
COPY . .

# Set the command to run the Flask application
CMD ["python", "main.py"]
