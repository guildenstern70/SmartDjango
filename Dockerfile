FROM python:3.8-slim-buster
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
ADD . .
EXPOSE 8080
CMD echo "make migrations"
CMD python manage.py makemigrations
CMD echo "migrate"
CMD python manage.py migrate
CMD echo [$0] Starting Django Server...
CMD exec gunicorn -w 3 SmartDjango.wsgi:application --bind 0.0.0.0:8080
