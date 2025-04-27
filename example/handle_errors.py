import requests
from requests.exceptions import RequestException

try:
    response = requests.get("https://jsonplaceholder.typicode.com/nonexistent", timeout=5)
    response.raise_for_status()  # Проверяет, был ли запрос успешным (код 200-299)
    print(response.json())
except requests.exceptions.HTTPError as err:
    print(f"HTTP ошибка: {err}")
except requests.exceptions.Timeout:
    print("Таймаут запроса")
except RequestException as err:
    print(f"Ошибка при выполнении запроса: {err}")