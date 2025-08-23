#!/usr/bin/env bash
set -e

# Install deps (Vercel also installs automatically, this ensures local parity if needed)
pip install -r requirements.txt

# Collect static files into ./staticfiles
python manage.py collectstatic --noinput

