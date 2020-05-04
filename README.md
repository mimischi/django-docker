# Develop and deploy Django applications with Docker

[![Build Status](https://travis-ci.org/mimischi/django-docker.svg?branch=master)](https://travis-ci.org/mimischi/django-docker) [![codecov](https://codecov.io/gh/mimischi/django-docker/branch/master/graph/badge.svg)](https://codecov.io/gh/mimischi/django-docker) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

This repository is used to test a new project layout to develop Django
applications within Docker containers. To be very fancy, we're also using
`poetry.toml` instead of `requirements.txt` for our Python dependencies. Deployment
to production is handled by a remote [Dokku](http://dokku.viewdocs.io/dokku/)
instance.

## Details

We're using `Python 3.7-slim` for the base image as a trade-off of container size and build time.
 Further we utilize [`poetry`](https://github.com/python-poetry/poetry) to try out a new approach
  of Python requirement management.

## Features

* Develop inside of Docker containers! (Both Django and PostgreSQL run inside of
  their own containers)
* Django `runserver_plus` is sequentially restarted, if the application crashes
  for any reason.
* Use `Makefile` for common commands (`docker-compose build`, `python manage.py
  makemessages`, ...).
* Uses [WhiteNoise](http://whitenoise.evans.io/en/stable/) to manage static
  files.
* Run continuous integration of Travis-CI.
* Deploy to [Dokku](https://github.com/dokku/dokku) for production.
* Use [Sentry](https://sentry.io/) for error reporting on your production
  instance.
  * **Psssst! You can easily run your own [Sentry instance on
  Dokku](https://github.com/mimischi/dokku-sentry)!**

**Note: In the current layout, with the `Dockerfile` residing under
`./docker/dokku/Dockerfile`, you will need to install the
[`dokku-dockerfile`](https://github.com/mimischi/dokku-dockerfile) plugin and
set the path accordingly.****

### Planned

* It would be neat to get [Celery](http://www.celeryproject.org/) to work.

# Usage

## Local development

Running `make build` will download all required images (`python:3.7-slim` and
`postgresql:9.6-alpine`) and build the app. Next you need to run `make migrate` to run
all database migrations, after which you can actually start using this project.
Running `docker-compose up` will collect all staticfiles and start both
services. The app will be available via [localhost:8000](http://localhost:8000).

## Deployment to production (via Dokku)

### Prepare app on Dokku host

Before deployment, one needs to set up the app and PostgreSQL database on the
Dokku host. For the sake of simplicity we're going to name the Dokku app
`djangodocker` in this example.

```
# Create app
$ dokku apps:create djangodocker

# Create PostgreSQL database and link it to the app
$ dokku postgres:create djangodocker-postgres
$ dokku postgres:link djangodocker-postgres djangodocker

# Set the bare minimum configuration
$ dokku config:set --no-restart djangodocker DJANGO_ADMIN_URL="/admin"
$ dokku config:set --no-restart djangodocker DJANGO_ALLOWED_HOSTS=djangodocker.example.com
$ dokku config:set --no-restart djangodocker DJANGO_SECRET_KEY=$(echo `openssl rand -base64 100` | tr -d \=+ | cut -c 1-64)
$ dokku config:set --no-restart djangodocker DJANGO_SETTINGS_MODULE=config.settings.production
$ dokku config:set --no-restart djangodocker DJANGO_SENTRY_DSN=https://your:sentry-dsn@sentry.com/1234
# Make sure the plugin `dokku-dockerfile` is installed
$ dokku dockerfile:set djangodocker docker/dokku/Dockerfile
```

You may also need to set the domain using `dokku domains:set djangodocker
djangodocker.example.com`.

### Setup Dokku server as `git remote`

To successfully push your app to the Dokku host, you need to set up the server
as a `git remote`:

`git remote add dokku dokku@djangodocker.example.com:djangodocker`

### Deployment

Deploying the `master` branch of the app is straightforward:

`git push dokku master`

If you want to deploy another branch (e.g. `newfeature`), you need to use this
syntax:

`git push dokku newfeature:master`

More information can be found in the [official Dokku
documentation](http://dokku.viewdocs.io/dokku/getting-started/installation/).
