# Use an official Python runtime as the base image
FROM python:3.10.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Create a virtual environment
RUN python -m venv streamlit

# Activate the virtual environment and install packages
RUN /app/streamlit/bin/pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Make port 8501 available to the world outside this container
EXPOSE 8501

# Define the command to run the app when the container starts
CMD ["/app/streamlit/bin/python", "-m", "streamlit.cli", "run", "streamlit_app.py"]
