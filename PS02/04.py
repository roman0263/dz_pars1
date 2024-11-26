import requests

# URL для отправки POST-запроса
url = "https://jsonplaceholder.typicode.com/posts"

# Данные для создания нового поста
data = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}

# Выполняем POST-запрос с передачей данных
response = requests.post(url, json=data)

# Печатаем статус-код ответа
print("Статус-код ответа:", response.status_code)

# Печатаем содержимое ответа
try:
    response_data = response.json()  # Преобразуем ответ в JSON
    print("Ответ сервера:")
    print(response_data)
except ValueError:
    print("Не удалось преобразовать ответ в JSON.")
