# Machine-Learning-and-Statistics-Project 2020

***


### Project Objective
Create a web service that uses machine learning to make predictions based on the data set powerproduction available on Moodle. The goal is to produce a model that accurately predicts wind turbine power output from wind speed values, as in the data set. A web service is then developed that responds with predicted power values based on speed values sent as HTTP requests.

###  Repository contents:

1. Jupyter notebook investigating the power production dataset and associated models
2. server.py  that runs the web service based on the model:
3. Dockerfile to build and run the web service in a container
4. The power production dataset (csv file)
5. Python scripts that runs the web service based on the model:
6. requirements.txt is a requirements file for the virtual environment and Docker container
7. staticpages folder of which index.html is the home page of the flask server
8. Readme

#### Create Virtual Enviromment

- python -m venv venv
- .\venv\Scripts\activate.bat
- set FLASK_APP=server
- set FLASK_ENV=development (if you wish to run in a development environment)
- flask run


#### Build Docker

docker build . -t server-app
docker run -d -p 5000:5000 server-app



#### Downloading the Repository

To download it, do the following:

    Click on the "Clone or Download" button
    Select "Download ZIP". This will open a prompt allowing you to save the file to your computer.
    Navigate to the download location and extract the compressed (.zip) folder to a suitable location.
