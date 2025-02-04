#!/bin/sh
set -e  # Exit on any error

# Start Nginx
echo "Starting Nginx..."
service nginx start

# Run database migrations
echo "Running database migrations..."
flask db upgrade

# Start Flask app
echo "Starting Flask application..."
exec flask run --host=0.0.0.0