FROM python:3.7-slim
ARG DJANGO_SETTINGS_MODULE
ARG DJANGO_ADMIN_URL
ARG DJANGO_SECRET_KEY
ARG DATABASE_URL
ARG DJANGO_SENTRY_DSN
ENV PYTHONBUFFERED=1 DJANGO_SETTINGS_MODULE=${DJANGO_SETTINGS_MODULE} DJANGO_ADMIN_URL=${DJANGO_ADMIN_URL} DJANGO_SECRET_KEY=${DJANGO_SECRET_KEY} DATABASE_URL=${DATABASE_URL} DJANGO_SENTRY_DSN=${DJANGO_SENTRY_DSN} POETRY_VERSION=1.0.5 POETRY_VIRTUALENVS_CREATE=false

# Add new user to run the whole thing as non-root
RUN groupadd app
RUN adduser --ingroup app --home /app --disabled-password --gecos "" app

# Install build dependencies
RUN apt update \
	&& apt install -y gettext


# Set the correct timezone
RUN cp /usr/share/zoneinfo/Europe/Berlin /etc/localtime \
    && echo "Europe/Berlin" > /etc/timezone

# Copy Pipfile and install python dependencies
COPY --chown=app:app pyproject.toml poetry.lock /
RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
RUN PATH="$PATH:$HOME/.poetry/bin" && poetry install

# Copy dokku specific files to the project root
COPY --chown=app:app docker/dokku/* /app/
COPY --chown=app:app docker/dokku/entrypoint.sh /
RUN chmod +x entrypoint.sh /app/deploy.sh

USER app
WORKDIR /app

# Copy all related app files
COPY --chown=app:app . /app

ENTRYPOINT ["/entrypoint.sh"]
