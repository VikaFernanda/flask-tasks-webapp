#!/bin/sh

# Exit on any error
set -e

# echo "Waiting for the database to be ready..."
# sleep 5

echo "Running database migrations..."
flask db upgrade

echo "Starting Nginx..."
service nginx start

echo "Starting Flask app..."
exec flask run --host=0.0.0.0