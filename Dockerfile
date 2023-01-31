# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/





# # base image
# FROM python:3.8
# # setup environment variable
# ENV DockerHOME=/home/app/webapp
#
# # set work directory
# RUN mkdir -p $DockerHOME
#
# # where your code lives
# WORKDIR $DockerHOME
#
# # set environment variables
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1
#
# # install dependencies
# RUN pip install --upgrade pip
#
# # copy whole project to your docker home directory.
# COPY . $DockerHOME
# # run this command to install all dependencies
# RUN pip install -r requirements.txt
# # port where the Django app runs
# EXPOSE 8000
# # start server
# CMD python manage.py runserver





# FROM python: 3.10
# ENV PYTHONDONTWRITEBYTECODE=1
# ENV PYTHONUNBUFFERED=1
# ENV PORT=8000
#
# WORKDIR /app
#
# COPY ./requirements.txt/app/
# RUN pip install --upgrade pip
# RUN pip install -r requirements.txt
# COPY /app
# RUN python manage.py collectstatic
# CMD gunicorn oc_lettings_fr.wsgi:application --bind @.0.0.0:$PORT





# syntax=docker/dockerfile:1
# FROM node:18-alpine
# WORKDIR /app
# COPY . .
# RUN yarn install --production
# CMD ["node", "src/index.js"]
# EXPOSE 3000