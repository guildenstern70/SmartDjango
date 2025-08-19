# SmartDjango

![SmartDjango CI](https://github.com/guildenstern70/SmartDjango/workflows/SmartDjango%20CI/badge.svg)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/56d6e895837d4fcc93387e33eb774adc)](https://www.codacy.com/gh/guildenstern70/SmartDjango/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=guildenstern70/SmartDjango&amp;utm_campaign=Badge_Grade)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Description
Template solution for Django Web App with:

1. Django v.4.0.x
2. Bootstrap v.5
3. SQLite

## Download required libraries

    pip install -r requirements.txt
 
## App Setup
    
Create Application database and data definitions:

    python manage.py makemigrations
    python manage.py migrate
    
## Admin App

If not already done, create super-user with

    python manage.py createsuperuser
    
If unsure, try with "admin/admin"

## Local Run
Run locally within Django sandbox:

    ./run.sh

## Run with Docker

    docker build --platform linux/amd64 -t smart-django:x .
    docker run -p 8080:8080 smart-django:1

    