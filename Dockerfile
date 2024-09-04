# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Define environment variables
ENV GITHUB_TOKEN=your_github_token
ENV GITHUB_REPOS=owner1/repo1,owner2/repo2,owner3/repo3

# Run the exporter when the container launches
CMD ["python", "github_actions_exporter.py"]
