import requests
import pprint
response = requests.get(url="https://api.github.com")
# print (response.status_code)
# if response.ok :
#     print("Запрос выполнен успешно")
# else:
#     print("Произошла ошибка")

print(response.text)
response_json = response.json()
pprint.pprint(response_json)