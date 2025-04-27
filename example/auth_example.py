import requests
from requests.auth import HTTPBasicAuth

# Basic Auth
response = requests.get(
    "https://httpbin.org/basic-auth/user/passwd",
    auth=HTTPBasicAuth("user", "passwd")  # или auth=("user", "passwd")
)
print("Basic Auth:", response.json())

# Bearer Token
headers = {"Authorization": "Bearer YOUR_TOKEN"}
response = requests.get("https://api.example.com/protected", headers=headers)
print("Bearer Token:", response.json())