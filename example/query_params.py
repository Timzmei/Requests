import requests

params = {
    "page": 1,
    "limit": 10,
    "sort": "desc"
}

response = requests.get("https://jsonplaceholder.typicode.com/posts", params=params)
print("Полный URL:", response.url)  # https://jsonplaceholder.typicode.com/posts?page=1&limit=10&sort=desc
print("Данные:", response.json())