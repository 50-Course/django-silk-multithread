FROM python:3.11-slim-buster

WORKDIR /app

COPY . .

RUN pip install pipenv
RUN pipenv sync