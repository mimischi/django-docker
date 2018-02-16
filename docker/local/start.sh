#!/bin/sh

while true; do
    echo "Re-starting Django runserver_plus!"
    python manage.py runserver_plus 0.0.0.0:8000
    sleep 2
done
