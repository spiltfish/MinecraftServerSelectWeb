#!/usr/bin/env bash
##
# Version: 1.0
# Author:  jeffreyrobertbean@gmail.com
# Date:    11/04/2015
##

# Simple retry function
function retry {
  local n=1
  local max=5
  local delay=10
  while true; do
    "$@" && break || {
      if [[ ${n} -lt ${max} ]]; then
        ((n++))
        echo "Migration failed. Attempt $n/$max:"
        sleep ${delay};
      else
        echo "The command has failed after $n attempts."
        exit 1
      fi
    }
  done
}
## Validate the django project is going to load properly (does not mean it will run)



python manage.py validate
###
# migrate db, so we have the latest db schema
#
#  Need to retry so if postgres is starting for the first time.
#  Also allows time to see any errors before it attempts to start the server.
##
retry python manage.py migrate --noinput


## Collect all the static files.
python manage.py collectstatic --noinput

##
# start server on the docker ip interface, port 8001
#  Also handles if we are going to start the production gunicorn server or the develop server
##
DJANGO_DEBUG_MODE=True
#TODO: remove this set to true so production server can be configured
if [ -z ${DJANGO_DEBUG_MODE} ]; then
    su -m djuser -c "gunicorn davy.wsgi -w 4 -b 0.0.0.0:8001 --chdir=/code --enable-stdio-inheritance
    --error-logfile -"
else
    python manage.py runserver 0.0.0.0:8000
fi