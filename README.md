# Hanisa Course Project


## Be aware of:
1. Database configuration


## Install the dependencies first before running the project
1. Run `pipenv install` from the project root directory.
2. Run `npm install` within the `/static/` directory.


## The easiest way to run this project
Assume that you've already had user `dbadmin` in the database.
```
$ sudo -u postgres createdb hanisa-course --owner dbadmin --password
$ python3 manage.py migrate
$ python3 manage.py createsuperuser
$ python3 manage.py runserver
```
