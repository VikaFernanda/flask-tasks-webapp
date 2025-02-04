#!/bin/sh
set -e  # Exit immediately if a command exits with a non-zero status

# Start Nginx
echo "Starting Nginx..."
service nginx start

# Wait for PostgreSQL (if needed)
# echo "Waiting for database..."
# sleep 5  # Uncomment if your database isn't ready instantly

# Run database migrations
echo "Running database migrations..."
flask db upgrade

# Start Flask app
echo "Starting Flask application..."
exec flask run --host=0.0.0.0