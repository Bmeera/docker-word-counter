# Use Python as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the script into the container
COPY word_counter.py .

# Define the command to run the script
CMD ["python", "word_counter.py"]

