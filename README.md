## SmartDjango

![SmartDjango CI](https://github.com/guildenstern70/SmartDjango/workflows/SmartDjango%20CI/badge.svg)

#### Description
Template solution for Django Web App with:

1. Django v.3.x.y
2. Bootstrap v.5
3. SQLite

### Download required libraries

    pip install -r requirements.txt
 
##### App Setup
    
Create Application database and data definitions:

    python manage.py migrate
    
#### Admin App

If not already done, create super-user with

    python manage.py createsuperuser
    
If unsure, try with "admin/admin"

#### Local Run
Run locally within Django sandbox:

    ./run.sh

#### Create Docker image

    docker build -t smart-django:1 .
    
#### Run image

    docker run -p 8080:8080 smart-django:1
    



    