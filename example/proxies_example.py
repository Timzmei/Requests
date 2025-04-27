import requests

proxies = {
    "http": "http://10.10.1.10:3128",  # HTTP-прокси
    "https": "http://10.10.1.10:1080",  # HTTPS-прокси
}

try:
    response = requests.get("http://example.com", proxies=proxies, timeout=5)
    print(response.text)
except requests.exceptions.ProxyError:
    print("Ошибка подключения к прокси")