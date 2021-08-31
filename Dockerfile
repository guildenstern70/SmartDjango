FROM python:3.9-slim-buster
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8080
RUN chmod 664 .
RUN chmod +x run_unicorn.sh
ENTRYPOINT ["/bin/bash", "/app/run_unicorn.sh"]
