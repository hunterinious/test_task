# test_task

## Setup virtual environment

To create a virtual environment you need to type the following command in the root directory:

`python3 -m venv env`

Then we need to activate the virtual environment:

`source env/bin/activate`

Finally you need to install all the necessary requirements:

`pip install -r requirements.txt`


## Setup db 

First you need to create the database, go to root directory and type:

`docker-compose up db`

Then we need to run all migrations to create all required tables:

`python3 manage.py migrate`


## Run app

In the root directory type the following command:

`python3 manage.py runserver`
