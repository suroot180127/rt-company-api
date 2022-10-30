# The image you are going to inherit your Dockerfile from
FROM python:3.9.5
# Necessary, so Docker doesn't buffer the output and that you can see the output 
# of your application (e.g., Django logs) in real-time.
ENV PYTHONUNBUFFERED 1

# Set the /testapp directory as the working directory
WORKDIR /testapp
# Copies from your local machine's current directory to the testapp folder 
# in the Docker image
COPY . .
# Copy the requirements.txt file adjacent to the Dockerfile 
# to your Docker image
COPY ./requirements.txt /requirements.txt
# Install the requirements.txt file in Docker image
RUN pip install -r /requirements.txt

