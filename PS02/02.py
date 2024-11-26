import requests
import pprint

# URL для обращения к API
url = "https://api.github.com/search/repositories"

# Параметры запроса: ищем репозитории, содержащие HTML в названии
params = {"q": "html"}

# Выполняем GET-запрос
response = requests.get(url, params=params)

# Печатаем статус-код ответа
print("Статус-код ответа:", response.status_code)

# Печатаем содержимое ответа в формате JSON
try:
    json_data = response.json()  # Преобразуем ответ в JSON
    print("Содержимое ответа:")
    pprint.pprint(json_data)
except ValueError:
    print("Не удалось преобразовать ответ в JSON.")
