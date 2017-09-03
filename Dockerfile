FROM python:3.6.2-alpine3.6
ENV PYTHONBUFFERED 1

# Add new user to run the whole thing as non-root
RUN addgroup -S app
RUN adduser -G app -h /app -D app

# Copy Pipfile and install system-wide
# We're installing system-wide, because we currently have problems
# correctly using the entrypoint.sh, while activating the virtual environment
COPY Pipfile /app
WORKDIR /app

# Install build dependencies for PostgreSQL. While we're at it, also install
# pipenv and all python requirements. Then remove unneeded build dependencies.
RUN apk update \
    && apk add --no-cache --virtual .build-deps \
       gcc \
       musl-dev \
    && apk add postgresql postgresql-dev \
    && pip install pipenv \
    && pipenv install --system \
    && apk del .build-deps

# Change to user and copy code
USER app
COPY . /app
COPY docker/dokku/* /app
