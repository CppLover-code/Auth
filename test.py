import requests

response = requests.post(
    "http://127.0.0.1:5000/register",
    json={
        "username": "mark",
        "password": "1234"
    }
)

print(response.text)
print(response.status_code)