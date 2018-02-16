FROM python:alpine3.6
ARG DJANGO_SETTINGS_MODULE
ARG DJANGO_ADMIN_URL
ARG DJANGO_SECRET_KEY
ARG DATABASE_URL
ARG DJANGO_SENTRY_DSN
ENV PYTHONBUFFERED=1 DJANGO_SETTINGS_MODULE=${DJANGO_SETTINGS_MODULE} DJANGO_ADMIN_URL=${DJANGO_ADMIN_URL} DJANGO_SECRET_KEY=${DJANGO_SECRET_KEY} DATABASE_URL=${DATABASE_URL} DJANGO_SENTRY_DSN=${DJANGO_SENTRY_DSN}

# Add new user to run the whole thing as non-root
RUN addgroup -S app \
    && adduser -G app -h /app -D app

# Install build dependencies
RUN apk update \
    && apk add bash \
    && apk add \
    && apk add --no-cache \
       gcc \
       musl-dev \
       zlib-dev \
       jpeg-dev \
       libxslt-dev \
       libxml2-dev \
       postgresql \
       postgresql-dev \
       jpeg \
       tzdata

# Set the correct timezone
RUN cp /usr/share/zoneinfo/Europe/Berlin /etc/localtime \
    && echo "Europe/Berlin" > /etc/timezone

# Copy Pipfile and install python dependencies
COPY --chown=app:app Pipfile Pipfile.lock /
RUN pip install pipenv
RUN LIBRARY_PATH=/lib:/usr/lib /bin/sh -c "pipenv install --system --deploy"

# Copy dokku specific files to the project root
COPY --chown=app:app docker/dokku/* /app/
COPY --chown=app:app docker/dokku/entrypoint.sh /
RUN chmod +x entrypoint.sh /app/deploy.sh

USER app
WORKDIR /app

# Copy all related app files
COPY --chown=app:app . /app

ENTRYPOINT ["/entrypoint.sh"]
