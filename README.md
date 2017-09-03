# Use Django with Docker

This repository is used to test a new repository layout to develop Django
applications with Docker containers. To bring it up to point, we're also using
Pipfiles instead of `requirements.txt` for our requirement needs.

## Details

We're using `Alpine Linux` for the base image, to start with a small container
size. The official python image `python:3.6.2-alpine3.6` provides the Python
interpreter. Further we utilize
[`pipenv`](https://github.com/kennethreitz/pipenv)) to try a new bleeding-edge
approach of Python requirement management.

## Current status

Currently the local development works using a dockerized default Django project
with a dockerized PostgreSQL instance.

For the production part, we'd like to create a deployment process to our
[Dokku](https://github.com/dokku/dokku) server, using a separate Dockerfile.

Maybe I'd also like to play around with [Travis-CI](https://travis-ci.org) and
an automatic deploy to our Dokku server using Travis-CI. Getting
[Celery](http://www.celeryproject.org/) to run would also be neat.

# Usage

## Local development

Running `docker-compose up --build -d` will build the app and postgress, migrate
and start it. It will then be available under
[localhost:8000](http://localhost:8000).
