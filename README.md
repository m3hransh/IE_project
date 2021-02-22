# IE Project
## Installation
```bash
# cloning the repo
$ git clone https://github.com/m3hransh/IE_project.git
$ cd IE_project
# create virtual-environment-name for python
$ python3 -m venv venv
# active virtual env
$ source venv/bin/activate # Linux and macOS
$ venv\Scripts\activate # Microsoft Windows
# Installing packages in the environment
$ pip install -r requirements.txt
# export follwoing environment variable
# Linux and macOS
$ export FLASK_APP=flasky.py 
$ export FLASK_ENV=development 
$ export DEV_DATABASE_URL=sqlite:////absolute/path/to/database 
# Microsoft Windows
$ set FLASK_APP=flasky.py # Microsoft Windows
$ set FLASK_ENV=development 
$ set DEV_DATABASE_URL=sqlite:///c:/absolute/path/to/databasee 

#notes
# You can use database of your choice if you would like
# MySQL -- DEV_DATABASE_URL= mysql://username:password@hostname/database
# Postgres -- DEV_DATABASE_URL= postgresql://username:password@hostname/database

```
## Blueprints
* ### main
    * `/` -- Dashboard page show the clickable table of all employees.
    * `/register` -- Form for registering new an employee.
    * `/edit[?uers_id=id]` -- You can edit employee base on Personel ID. It is also accessible through clicking table rows in "/" and "/report".
    * `/remove` -- Remove employee base on Personel ID.
    * `/report` -- You can query employees base on some fields.
    * `/stats` -- Show a summary of statisitics.

* ### auth
    * `/auth/login` -- Login page for Admin. All the main routes are protected and redirect to this.
    * `/auth/logout` -- Remove the login user from the session.

* ### api
    * `GET api/myget/<name>` -- Find all employees with following name.
    * `PUT api/myupdate/<int:id>/<int:income>` -- Update income of the employee with Personel ID equal to "id".
    * `DELETE api/mydel/(male|female)` -- Delete all male or female employees.


