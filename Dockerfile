FROM python:3.8-slim-buster
ENV PYTHONDONTRWRITBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir /app
WORKDIR /app
COPY requierments.txt /app/

RUN pip install --upgrade pip
RUN pip install -r requierments.txt

COPY ./core /app/

