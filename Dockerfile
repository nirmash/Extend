FROM python:3.11-slim-buster

WORKDIR .

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP = ./api/app.py

WORKDIR ./api

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0" , "--port=8080"]