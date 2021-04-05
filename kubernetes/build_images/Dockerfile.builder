FROM python:3.7.4

WORKDIR /app

COPY requirements.txt .

COPY ToDo app

RUN pip install -r requirements.txt
