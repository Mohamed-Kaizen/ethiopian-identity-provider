# Load Dump data

This tutorial is less or more important for the next tutorials. We will load pre data b/c we are lazy to add them manually.

## Load Users, Renew, Businesses

<div class="termy">
```console
$ python manage.py loaddata users_app_dumpdata.json --format=json

Installed 17 object(s) from 1 fixture(s)

Done :)
```
</div>


## Load Oauth Apps

<div class="termy">
```console
$ python manage.py loaddata oauth_app_dumpdata.json --format=json

Installed 4 object(s) from 1 fixture(s)

Done :)
```
</div>
