# Use the official Python 3.9 slim image as a base image
FROM python:3.9-slim

# Set the working directory inside the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# # List the files in the current directory to verify contents
# RUN ls -la /app  && sleep 10

# Install the Python packages specified in requirements.txt
RUN pip install -r scripts/requirements.txt

# Specify the command to run the Flask application
CMD ["flask", "run", "--host=0.0.0.0", "--reload"]
