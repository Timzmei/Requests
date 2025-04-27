# Библиотека Requests для Python

Requests - это HTTP-библиотека для Python, которая позволяет легко отправлять HTTP-запросы.

## Основные возможности

- Простая отправка HTTP-запросов из Python
- Кодирование и декодирование JSON
- Поддержка SSL-верификации
- Автоматическое декодирование содержимого
- Таймауты соединения
- HTTP-куки в стиле браузера
- Загрузка файлов с multipart-кодированием
- Вспомогательные методы для GET, POST, PUT, OPTIONS, DELETE запросов

## Отправка запросов

Импорт библиотеки:
```bash
import requests
```

## GET-запрос:

```python
response = requests.get('https://api.example.com/data')
```

### POST-запрос:
```python
payload = {'key1': 'value1', 'key2': 'value2'}
response = requests.post('https://api.example.com/data', data=payload)
```

## Работа с ответами
### Получить содержимое ответа как строку:
```python
html = response.text
```

### Получить JSON:
```python
data = response.json()
```

### Получить бинарное содержимое:
```python
image = response.content
```

## Коды состояния
### Проверка статус-кода:

```python
if response.status_code == 200:
    print('Успешно!')
elif response.status_code == 404:
    print('Не найдено.')
```

## Заголовки запросов
### Просмотр заголовков запроса:
```python
headers = response.request.headers
```

### Добавление кастомных заголовков:
```python
headers = {'User-Agent': 'Мой скрипт'}
response = requests.get(url, headers=headers)
```

## Параметры запроса
### Добавление параметров в URL:
```python
params = {'key1': 'value1', 'key2': 'value2'}
response = requests.get(url, params=params)
```

## POST-данные
### Отправка данных в теле запроса:
```python
data = {'key': 'value'}
response = requests.post(url, data=data)
```

### Отправка form-encoded данных:
```python
data = {'key1': 'value1', 'key2': 'value2'}
response = requests.post(url, data=data)
```

## Загрузка файлов
### Загрузка одного файла:
```python
files = {'file': open('report.xls', 'rb')}
response = requests.post(url, files=files)
```

### Загрузка нескольких файлов:
```python
files = {'file1': open('report.xls', 'rb'),
         'file2': open('data.json', 'rb')}
response = requests.post(url, files=files)
```

## Таймауты
### Установка таймаутов соединения:
```python
requests.get(url, timeout=3.05)
```

## Аутентификация
### HTTP Basic Auth:
```python
response = requests.get(url, auth=('user', 'pass'))
```

### OAuth1:
```bash
import requests_oauthlib
```

```python
oauth = requests_oauthlib.OAuth1('client_key', client_secret='secret')
response = requests.get(url, auth=oauth)
```

## Сессии
### Создание сессии для сохранения параметров между запросами:
```python
session = requests.Session()
session.params = {'key': 'value'}
response = session.get('http://httpbin.org/get')
```

## Обработка ошибок
### Проверка успешности запроса:
```python
if response.status_code == 200:
   # успешный запрос
elif response.status_code == 404:
   # обработка ошибки 404
```

### Перехват ошибок соединения:
```python
try:
   response = requests.get(url, timeout=3)
except requests.exceptions.ConnectionError:
   # обработка ошибки соединения
```

## SSL-верификация
### Проверка SSL-сертификата:
```python
response = requests.get(url, verify=True)
```

### Отключение предупреждений SSL:
```python
response = requests.get(url, verify=False)
```

## Прокси-серверы
### Запросы через прокси:
```python
proxies = {
   'http': 'http://10.10.1.1:3128',
   'https': 'http://10.10.1.1:1080'
}
requests.get(url, proxies=proxies)
```

## Дополнительные примеры запросов
### PUT-запрос:
```python
data = {'key':'value'}
response = requests.put('https://api.example.com/data', data=data)
```

### DELETE-запрос:
```python
response = requests.delete('https://api.example.com/data/1')
```

### HEAD-запрос:
```python
response = requests.head('http://example.com')
print(response.headers)
```

### OPTIONS-запрос:
```python
response = requests.options('https://api.example.com/data')
print(response.headers['Allow']) # разрешенные HTTP-методы
```

## Продвинутые техники
### Работа с сессиями
```python
session = requests.Session()
session.auth = ('username', 'password')

response = session.get('https://api.example.com/user')
# последующие запросы будут использовать аутентификацию
```

### Работа с куками
```python
url = 'http://example.com'
cookies = {'my_cookie': 'cookie_value'}
response = requests.get(url, cookies=cookies)
```

### Потоковая обработка ответа
```python
with requests.get(url, stream=True) as response:
    for chunk in response.iter_content(8192):
        print(chunk)
```

### Установка таймаутов и повторных попыток
```python
from requests.exceptions import ConnectionError

try:
    response = requests.get(url, timeout=3.05)
except ConnectionError as ce:
    response = requests.get(url, timeout=5)
```

## Альтернативные HTTP-библиотеки Python
### Сравнение популярных библиотек:
* requests - Самая популярная библиотека. Простой, интуитивный API, мощные функции
* urllib - Встроенная HTTP-библиотека Python. Низкоуровневая, менее удобная
* httpx - Основана на requests, добавляет async, HTTP/2, пул соединений
* aiohttp - Асинхронная HTTP-библиотека для asyncio
* httpie - Удобный HTTP-клиент для командной строки
* scrapy - Специализированный фреймворк для веб-скрапинга
### Рекомендации по выбору:
* requests - лучший универсальный выбор
* httpx - для асинхронных запросов
* aiohttp - для продвинутой асинхронности
* scrapy - для крупных проектов по скрапингу
