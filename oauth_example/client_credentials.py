"""An example using client credentials flow.

Allows an application to request an Access Token using its Client Id
and Client Secret. It is used for non interactive applications
(a CLI, a daemon, or a Service running on your backend) where the token is
issued to the application itself, instead of an end user.
"""
import requests

payload = {
    "grant_type": "client_credentials",
    "client_id": "viuQMZdwhTLJXvlma143KdhivQaqglC7qMp57eFW",
    "client_secret": "Z5kQEk1EvvHuxwLRz5MDaGCXAS5CSxn89uDmlKP9Vu7MADmlpelzfkFXtSXxjAwZMtV4mX9ZsxwQKrjJamF9QpFzLknKo1rzQ9wIHAP6qZBoBh0EFZETSctaoTMlsMXD",  # noqa B950
}

url = "http://127.0.0.1:8000/o/token/"

response = requests.post(url, data=payload)

print(response.json())
