# TA-CloudxLabs
A simple web application that accepts a name and email.
To run clone the repo and run using docker.

In the root directory,

$ docker compose -f docker-compose.dev.yml up

The flask server runs on port 8000 and the mysql server runs on 3306. It takes a few seconds for the flask and MySQL server to boot up.
To access the website, use the link in the terminal or localhost:8000

Append /view to show the entered data.
