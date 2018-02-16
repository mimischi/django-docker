FROM python:alpine3.6
# Tell python not to produce any `__pycache__` and `*.pyc` files
ENV PYTHONBUFFERED=1 PYTHONDONTWRITEBYTECODE=1 INSIDE_DOCKER=1

# Install all dependencies needed to install our python requirements
RUN apk update \
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
       gettext \
       tzdata

# Set the correct timezone
RUN cp /usr/share/zoneinfo/Europe/Berlin /etc/localtime \
    && echo "Europe/Berlin" > /etc/timezone

# Copy Pipfile, install pipenv and then install all python dependencies
COPY Pipfile Pipfile.lock /
RUN pip install pipenv
RUN LIBRARY_PATH=/lib:/usr/lib /bin/sh -c "pipenv install --dev --system"

# Copy the entrypoint.sh and start.sh and make them executable
COPY docker/local/entrypoint.sh docker/local/start.sh /
RUN chmod +x /entrypoint.sh /start.sh

# All subsequent commands will be run from the /app folder
WORKDIR /app

ENTRYPOINT ["/entrypoint.sh"]
