# Command

## Migration

<div class="termy">
```console
$ python manage.py makemigrations

Migrations for 'users':
  users/migrations/0001_initial.py
    - Create model CustomUser
    - Create model Renew
    ...

$ python manage.py migrate

Operations to perform:
  Apply all migrations: admin, auth, contenttypes, users, sessions
Running migrations:
  Rendering model states... DONE
  Applying users.0001_initial... OK
  ...

Done :)
```
</div>

## Create super user

<div class="termy">
```console
$ python manage.py createsuperuser

# username:$ mohamed
# email:$ mohamed@etp.com
# Password: $ 
# Repeat for confirmation: $ 

Done :)
```
</div>


## Running server

<div class="termy">
```console
$ python manage.py runserver

Performing system checks...

System check identified no issues (0 silenced).

July 27, 2020 - 15:50:53
Django version 3.0, using settings 'etp.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
</div>
