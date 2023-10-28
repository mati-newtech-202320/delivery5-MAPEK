# Use an official Python runtime as a parent image
FROM registry.access.redhat.com/ubi9/python-39

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY payment_MAPEK.py requirements.txt /app

# Install any needed packages specified in requirements.txt∫
RUN pip install  --no-cache-dir -U -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define the command to run your Python script
CMD ["python", "payment_MAPEK.py"]