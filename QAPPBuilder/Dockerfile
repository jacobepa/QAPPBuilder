# pull official base image
FROM python:3.13-slim

# set work directory
WORKDIR /srv/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y \
  gcc netcat libpq-dev postgresql-client \
  git make pkg-config libgsl-dev automake autoconf \
  && apt-get clean

  # install dependencies
RUN pip install --upgrade pip
COPY ./requirements_essential.txt .

# install temp dependencies for build of psycopg2 etc
RUN pip install -r requirements-essential.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .

# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/srv/app/entrypoint.sh"]
