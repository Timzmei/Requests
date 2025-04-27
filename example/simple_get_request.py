import requests

# Отправка GET-запроса
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

# Проверка статус-кода
if response.status_code == 200:
    print("Успешный запрос!")
    print("Ответ в JSON:", response.json())
else:
    print("Ошибка:", response.status_code)