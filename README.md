# Todo Application
Application has been built using Django

### Application setup
To setup this application, python3.7.5 or higher , postgresql should be up and running

### Install dependencies
1. Create an virtual env where you will install all the dependencies
1. Activate your virtualenv
1. Install pip-tools (pip install pip-tools)
1. Install requirements using pip-tools (pip-compile && pip-sync)

### Configuration
Create a .env file from env.backup and update configurations
### Database configuration
For Database configuration loading, dj-database-url package has been used.
```
# postgres://USER:PASSWORD@HOST:PORT/NAME
DATABASE_URL=postgres://todo:password@localhost:5432/todo
```
### Create super user
Use following command to create an admin user
```
python manage.py createsuperuser
```

### Run application
```
python manage.py runserver
```
### Check in browser
http://localhost:8000/api/v1/common/users/

http://localhost:8000/api/v1/tasks/

### Run Test
pytest -s -v --cov=.