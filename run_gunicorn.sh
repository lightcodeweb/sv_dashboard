#!/usr/bin/env bash
# Initialize options for gunicorn
OPTS=(
  --env FLASK_APP=sv_dashboard
  --env FLASK_ENV=development
  --access-logfile -
  --error-logfile -
  --log-level debug
  -b 127.0.0.1:8093
  --reload
)

#Run gunicorn
gunicorn "${OPTS[@]}" sv_dashboard.application:APP
