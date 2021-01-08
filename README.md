# Machine-Learning-and-Statistics-Project 2020

***


### Project Objective
Create a web service that uses machine learning to make predictions based on the data set powerproduction available on Moodle. The goal is to produce a model that accurately predicts wind turbine power output from wind speed values, as in the data set. A web service is then developed that responds with predicted power values based on speed values sent as HTTP requests.

###  Repository contents:

1. The power production dataset (csv file).
2. Jupyter notebook investigating and modelling the power production dataset.
3. requirements.txt listing requirements for the virtual environment and Docker container.
4. server.py  that runs the web service.
5. staticpages folder of which index.html is the home page of the flask server.
6. Dockerfile to build and run the web service in a container.
7. model.pkl - the serialised random forest output from the jupyter notebook
8. Readme


#### Download the Repository

Firstly, this repository needs to be downloaded.  Do the following:
- Go to https://github.com/mhurley100/Machine-Learning-Statistics-Tasks.git
-Click on the "Clone or Download" button
-Select "Download ZIP". This will open a prompt allowing you to save the file to your computer.
-Navigate to the download location and extract the compressed (.zip) folder to a suitable location.

#### Review the jupyter notebook 
- Review Machine Learning & Statistics Project 2020.ipynb file.  This provides an analysis of the relationship between wind speed and power output.

#### Open Web Service

This can be achieved by running the flask app either in a virtual enviroment or through Docker.

####  Virtual Environment

Create a virtual environment on the command line interface as follows:
- python -m venv venv
- .\venv\Scripts\activate.bat
- set FLASK_APP=server
- set FLASK_ENV=development (if you wish to run in a development environment)
- flask run

-Navigate to this website:

http://127.0.0.1:5000

- Input the speed value and click the calculate button.

#### Docker Container

Steps are as follows:
1. Build the docker image:          docker build -t server-app .
2. View Docker image:               docker image ls
3. View docker container            docker container ls
4. Run docker in detached mode:     docker run -d -p 5000:5000 server-app


 ### Licence 
 
 This project is licensed under GNU GENERAL PUBLIC LICENSE