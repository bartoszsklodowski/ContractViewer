#!/bin/bash

# Apply database migrations
echo "Apply database migrations"
python manage.py makemigrations
python manage.py migrate

# Load data to database
echo "Load data to database"
python manage.py loaddata fixtures.json

