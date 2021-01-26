FROM python:3.8-buster

ENV PYTHONUNBUFFERED 1

COPY ./docker/python/requirements.txt /requirements.txt

RUN apt-get install default-libmysqlclient-dev
RUN pip install -r /requirements.txt

RUN mkdir /btre
WORKDIR /btre
COPY ./btre /btre

RUN useradd user

USER user
