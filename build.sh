#!/usr/bin/env bash
set -e
# Do NOT install here; Vercel already installed from requirements.txt
python3 manage.py collectstatic --noinput
