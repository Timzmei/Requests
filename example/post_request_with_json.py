import requests
import json

# Данные для отправки
payload = {
    "title": "Новый пост",
    "body": "Текст поста",
    "userId": 1
}

# Отправка POST-запроса с JSON
response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=payload  # автоматически кодирует в JSON и добавляет заголовок Content-Type
)

# Вывод результата
print("Статус:", response.status_code)
print("Ответ сервера:", response.json())