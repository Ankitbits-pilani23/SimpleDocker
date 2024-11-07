# Flask Login Application

This is a simple Flask application with a login page, designed to be run in a Docker container. It demonstrates basic form handling in Flask and how to containerize a web application with Docker.

## Features

- Simple login form with username and password fields
- Basic session management and error handling with Flask flash messages
- Dockerized for easy deployment
- Styled with CSS for an enhanced user experience

## Project Structure

flask_login_app/ ├── app.py # Main Flask application ├── Dockerfile # Docker configuration file ├── requirements.txt # Dependencies for the Flask app ├── static/ │ └── style.css # CSS for styling the login page └── templates/ └── login.html # HTML template for the login form


## Prerequisites

- [Docker](https://docs.docker.com/get-docker/) installed on your machine
- Basic understanding of Python and Docker

## Setup and Run Instructions

2. Use the following command to build the Docker image:
docker build -t flask-login-app .

3. Run the container and map port 5000 from the container to your local machine:
docker run -p 5000:5000 flask-login-app

4. Access the Application
Open a web browser and go to http://localhost:5000

5. Test the Login Page
Enter the username "bits_admin" and password "welcome" to log in.
If credentials are correct, you’ll see a welcome message.
If credentials are incorrect, an error message will be displayed.

#### To remove the Docker image after testing:
docker rmi flask-login-app