import requests

url = "https://httpbin.org/post"
files = {"file": open("example.txt", "rb")}  # Файл должен существовать

response = requests.post(url, files=files)
print("Ответ сервера:", response.json())