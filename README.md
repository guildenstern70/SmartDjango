# SmartDjango

![SmartDjango CI](https://github.com/guildenstern70/SmartDjango/workflows/SmartDjango%20CI/badge.svg)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/56d6e895837d4fcc93387e33eb774adc)](https://www.codacy.com/gh/guildenstern70/SmartDjango/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=guildenstern70/SmartDjango&amp;utm_campaign=Badge_Grade)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Description
Template solution for Django Web App with:

1. Django v.5.x
2. Bootstrap v.5
3. SQLite

## Download required libraries

    pip install -r requirements.txt
 
## App Setup

There are several commands which you will use to interact with migrations and Django’s handling of database schema:

 - migrate, which is responsible for applying and unapplying migrations. 
 - makemigrations, which is responsible for creating new migrations based on the changes you have made to your models. 
 - sqlmigrate, which displays the SQL statements for a migration. 
 - showmigrations, which lists a project’s migrations and their status.

Create Application database and data definitions:

    python manage.py makemigrations  (Create new migrations based on the changes you have made to your models)
    python manage.py migrate (Apply and unapply migrations)
    python manage.py loaddata initial_data.yaml (Load initial data)
    

if you want to use PostgreSQL you must use the database name 'supabase':

    python manage.py makemigrations
    python manage.py migrate --database=supabase
    python manage.py loaddata initial_data.yaml --database=supabase

When database has been created, you can load initial data with:

    python manage.py loaddata initial_data.yaml
    
## Admin App

If not already done, create super-user with

    python manage.py createsuperuser
    
If unsure, try with "admin/admin"

## Local Run
Run locally within Django sandbox:

    ./run.sh

## Local run with PostgreSQL

1. Adjust settings.py to include the correct Supabase password.
2. Create an administrator account with 'createsuperuser' command.
3. Run the local development server with:

    DJANGO_DATABASE='supabase' python manage.py runserver



## Run with Docker

    docker build --platform linux/amd64 -t smart-django:x .
    docker run -p 8080:8080 smart-django:1

### Virtual Environment

Activate with

    source ./.venv/bin/activate

Deactivate with

    deactivate

### Crispy Forms

This project uses Crispy Forms for Bootstrap:

    https://django-crispy-forms.readthedocs.io/en/latest/


    