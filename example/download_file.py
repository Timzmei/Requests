import requests

url = "https://example.com/sample.pdf"
filename = "downloaded_file.pdf"

response = requests.get(url, stream=True)

if response.status_code == 200:
    with open(filename, 'wb') as file:
        for chunk in response.iter_content(1024):  # Загрузка по частям
            file.write(chunk)
    print(f"Файл сохранён как {filename}")
else:
    print("Ошибка загрузки:", response.status_code)