import requests
import pprint

# URL для обращения к API
url = "https://jsonplaceholder.typicode.com/posts"

# Параметры запроса: фильтруем записи по userId=1
params = {"userId": 1}

# Выполняем GET-запрос с параметрами
response = requests.get(url, params=params)

# Проверяем статус-код
print("Статус-код ответа:", response.status_code)

# Если запрос успешен, выводим полученные записи
if response.status_code == 200:
    try:
        data = response.json()  # Преобразуем ответ в JSON
        print("Полученные записи:")
        pprint.pprint(data)  # Форматированный вывод данных
    except ValueError:
        print("Не удалось преобразовать ответ в JSON.")
else:
    print(f"Ошибка при запросе. Статус-код: {response.status_code}")
