#!/bin/bash

# Build script for Vercel deployment
echo "Starting Django build process..."

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Run migrations (if needed)
python manage.py migrate --noinput

echo "Build completed successfully!"
