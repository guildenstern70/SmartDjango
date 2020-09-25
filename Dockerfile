FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

ADD . .

EXPOSE 8000

RUN chmod +x /app/run.sh
RUN /app/run.sh


