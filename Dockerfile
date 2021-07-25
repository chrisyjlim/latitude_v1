# syntax=docker/dockerfile:1

FROM python:3.9.6-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .



CMD [ "pytest" , "-vv"]

