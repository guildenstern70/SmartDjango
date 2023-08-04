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

    docker build -t smart-django:1 .
    docker run -p 8080:8080 smart-django:1

### Run in Kubernetes (minikube)

You may use any Kubernetes cluster, or install 'minikube' locally:

    https://minikube.sigs.k8s.io/docs/start/

then

    minikube start

Setup PostgreSQL pod:

    kubectl apply -f k8s/postgres/volume.yaml
    kubectl apply -f k8s/postgres/volume_claim.yaml
    kubectl apply -f k8s/postgres/secrets.yaml
    kubectl apply -f k8s/postgres/deployment.yaml
    kubectl apply -f k8s/postgres/service.yaml

Setup Django pod:

    docker build -t smart-django:1 .

Now you should push this image on some Container Registry. For your convenience, this image has been
already pushed to Docker Hub, so you may skip this step.

    docker tag smart-django:1 <your-registry>/smart-django:k8s
    docker push <your-registry>/smartdjango:k8s

Now you can deploy the Django pod:

    kubectl apply -f k8s/django/deployment.yaml
    kubectl apply -f k8s/django/service.yaml

See django logs with:

    kubectl logs -f django-<pod-id>

### Reset Kubernetes resources

    kubectl delete -f k8s/django/service.yaml
    kubectl delete -f k8s/django/deployment.yaml
    kubectl delete -f k8s/postgres/service.yaml
    kubectl delete -f k8s/postgres/deployment.yaml
    kubectl delete -f k8s/postgres/secrets.yaml
    kubectl delete -f k8s/postgres/volume_claim.yaml
    kubectl delete -f k8s/postgres/volume.yaml

It is recommended, if you are using minikube, to remove all resources:

    minikube delete

### Access the App

    minikube service django-service

### Connect to PostgreSQL pod

    kubectl exec -it postgres-<pod-id> -- psql -U django -d postgres

### Connect to Django pod

    kubectl exec -it django-<pod-id> -- /bin/bash
    

    



    