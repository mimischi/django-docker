# Use Django with Docker

This repository is used to test a new project layout to develop Django
applications within Docker containers. To be very fancy, we're also using
`Pipfile` instead of `requirements.txt` for our Python dependencies.

## Details

We're using `Alpine Linux` for the base image, to start with a small container
size. The official Python image `python:3.6.2-alpine3.6` provides the Python
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

Running `docker-compose up --build -d` will build the app and PostgreSQL,
collect all staticfiles and start both services. It will then migrate the Django
models to the database. The app will then be available under
[localhost:8000](http://localhost:8000).

## Deployment to production (via Dokku)

### Prepare app on Dokku host

Before deployment, one needs to set up the app and PostgreSQL database on the
Dokku host. For the sake of simplicity we're going to name the Dokku app
`djangodocker`.

```
# Create app
$ dokku app:create djangodocker

# Create PostgreSQL database and link it to the app
$ dokku postgres:create djangodocker-postgres
$ dokku postgres:link djangodocker-postgres djangodocker

# Set the bare minimum configuration
$ dokku config:set --no-restart djangodocker DJANGO_ADMIN_URL="/admin"
$ dokku config:set --no-restart djangodocker DJANGO_ALLOWED_HOSTS=djangodocker.example.com
$ dokku config:set --no-restart djangodocker DJANGO_SECRET_KEY=$(echo `openssl rand -base64 64` | tr -d ' ')
$ dokku config:set --no-restart djangodocker DJANGO_SETTINGS_MODULE=config.settings.production
```
You may also need to set the domain using `dokku domain:set djangodocker djangodocker.example.com`.

### Setup Dokku server as `git remote`

To successfully push your app to the Dokku host, you need to set up the server
as a `git remote`:

`git remote add dokku dokku@djangodocker.example.com:djangodocker`

### Deployment

Deploying the `master` branch of the app is straightforward:

`git push dokku master`

If you want to deploy another branch (e.g. `newfeature`), you need to use this syntax:

`git push dokku newfeature:master`

More information can be found in the [official Dokku documentation](http://dokku.viewdocs.io/dokku/getting-started/installation/).
