"""An example using password flow.

Since the Resource Owner Password Grant (ROPG) flow involves the client handling
the user's password, it must not be used by third-party clients. In this flow,
the user's username and password are exchanged directly for an Access Token.
"""
import requests

payload = {
    "grant_type": "password",
    "username": "kaizen",
    "password": "1234567899mnm",
    "client_id": "riZ8Bcesu8GaTq8qL6I5oJxeWarZzDcDzZnIOrya",
}

url = "http://127.0.0.1:8000/o/token/"

user_info_url = "http://127.0.0.1:8000/api/users/o/userinfo/"

response = requests.post(url, data=payload)

data = response.json()

print(data)

headers = {"Authorization": f"Bearer {data.get('access_token')}"}

user_info_response = requests.get(user_info_url, headers=headers)

print("=" * 100)
print(user_info_response.json())
