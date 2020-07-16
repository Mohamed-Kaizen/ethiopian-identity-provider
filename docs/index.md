> ## 🛠 Status: In Development
> Ethiopian Identity Provider is currently in development. So we encourage you to use it and give us your feedback, but there are things that haven't been finalized yet and you can expect some changes.
>
> See the list of Known Issues and TODOs, below, for updates.

## Overview

Ethiopian Identity Provider platform


## Getting Started

* [Fork repository][Ethiopian Identity Provider] and clone it.

```shell tab="Shell or CMD"

git clone https://github.com/Mohamed-Kaizen/etp
```

* install dependence:

```shell tab="Poetry"
poetry install
```

* serve the app:

create .env in the root of the project or set your ENV add the following line into .env file or set your ENV:
    
    DEBUG=True  # change this in production
    ALLOWED_HOSTS=example.com, localhost, 0.0.0.0, 127.0.0.1  # change this in production
    SECRET_KEY=w86k@*ash*z)dsxsoz+o*ne*ugb08(4nu13%8!m*+2_e@@7hnx  # change this in production and never put the production key here
    DATABASE_URL=sqlite:///db.sqlite3
    EMAIL_USER=example@example.com
    EMAIL_PASSWORD=''
    DROPBOX_OAUTH2_TOKEN=''


```shell tab="shell or CMD"

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

enjoy :)

# License: MIT


[Ethiopian Identity Provider]: https://github.com/Mohamed-Kaizen/etp
