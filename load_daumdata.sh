#!/usr/bin/env bash

./manage.py loaddata group_app_dumpdata.json --format=json
./manage.py loaddata users_app_dumpdata.json --format=json
./manage.py loaddata oauth_app_dumpdata.json --format=json
