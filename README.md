# Bussiness-Plan
financial solutions where users will answer a questionnaire and a business plan will be generated for them.
# Entities & Schema ERD Diagram 

https://drawsql.app/development-9/diagrams/business-plan#

# How To Operate Locally 

- machine with Python 3.10 and pip3 package manager
- install pipenv for createing and mainuplating virtualenvs `pip install pipenv`
- clone project from github
- change to project folder `cd Bussiness-Plan`
- type `pipenv shell`
- install dependancies or
- type pipenv `install -r requirements.txt`
- change to app directory cd bussiness_plan
- install libpq-dev on ubuntu `sudo apt install -y libpq-dev`
- login to postgresql server with password `sudo -u postgres psql`
- create database with name for example plan `CREATE DATABASE plan`
- create user with name for example app and password for example mypassword `postgres=# create user app with encrypted password 'mypassword';`
- grant privileges on database plan to user app `postgres=# grant all privileges on database plan to app;`
- map django orm to database python manage.py makemigrations
- apply orm migrations python manage.py migrate
- create superuser for admin panal python manage.py createsuperuser go with prompts
- start development server python manage.py runserver 0.0.0.0:8000

# Request & Response Cycle
- postman collection for various request and response in different testcases
- https://www.getpostman.com/collections/958b667540cdbbbacc40
# URLs for services

- for admin panal `http://127.0.0.1:8000/admin/`
- for login with jwt `http://127.0.0.1:8000/api/token/`
- for register new user `http://127.0.0.1:8000/user/` 
- for retrieveing allquestion and filter by section `http://127.0.0.1:8000/question/` 
- for filter question as per section `http://127.0.0.1:8000/question/?name=section_2`
- for add answer for question `http://127.0.0.1:8000/plan/`
- for retrieve user questions & answers get `http://127.0.0.1:8000/question/`

# Project Build
- this project build using Python 3.8.10
- python Django for web applications
- machine with ubuntu 20.04
