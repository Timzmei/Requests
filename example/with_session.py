import requests

# Создание сессии
session = requests.Session()
session.headers.update({"User-Agent": "MyApp/1.0"})  # Общие заголовки

# Первый запрос (сохраняет куки)
response1 = session.get("https://httpbin.org/cookies/set/sessioncookie/123456789")
print("Куки после первого запроса:", session.cookies.get_dict())

# Второй запрос (использует те же куки)
response2 = session.get("https://httpbin.org/cookies")
print("Куки сервера:", response2.json())