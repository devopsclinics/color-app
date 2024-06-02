# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Install any needed packages
RUN pip install flask colored

# Copy the Python script into the container
COPY app.py /app

# Set environment variables
ENV COLOR=blue

# Expose port 5000
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]




