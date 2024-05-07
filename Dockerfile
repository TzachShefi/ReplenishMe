# Use the official Python image as a base
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Install git to clone the repository
RUN apt-get update && apt-get install -y git

# Clone the repository containing your Python script and requirements file
RUN git clone https://github.com/TzachShefi/ReplenishMe.git .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the Python script when the container starts
CMD ["python", "helloworldindocker.py"]
