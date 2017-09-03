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

The project can also be deployed to [Dokku](https://github.com/dokku/dokku), using the `Dockerfile` in the root of this repository.

In the future I'd also like to play around with
[Travis-CI](https://travis-ci.org) and an automatic deploy to our Dokku server
using Travis-CI. Getting [Celery](http://www.celeryproject.org/) to run would
also be neat.

# Usage

## Local development

Running `docker-compose up --build -d` will build the app and postgress, migrate
and start it. It will then be available under
[localhost:8000](http://localhost:8000).

## Deployment to production (via Dokku)

After setting up the dokku server as a `git remote`, one needs to set up the app
on the remote machine.

```
# Create app
$ dokku app:create djangodocker

# Create PostgreSQL database and link it to the app
$ dokku postgres:create djangodocker-postgres
$ dokku postgres:link djangodocker-postgres djangodocker

# Set the bare minimum configuration
$ dokku config:set --no-restart DJANGO_ADMIN_URL="/admin"
$ dokku config:set --no-restart DJANGO_ALLOWED_HOSTS=djangotest.example.com
$ dokku config:set --no-restart DJANGO_SECRET_KEY=$(openssl rand -base64 64)
$ dokku config:set --no-restart DJANGO_SETTINGS_MODULE=config.settings.production
```

Afterwards deploying the usual way via `git push` pushes the app to production.
