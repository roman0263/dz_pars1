import requests
from bs4 import BeautifulSoup


# Создаём функцию, которая будет получать информацию
def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверка статуса ответа

        # Создаём объект Soup
        soup = BeautifulSoup(response.content, "html.parser")
        # Получаем слово
        english_words = soup.find("div", id="random_word")
        word_definition = soup.find("div", id="random_word_definition")

        if english_words and word_definition:
            return {
                "english_words": english_words.text.strip(),
                "word_definition": word_definition.text.strip()
            }
        else:
            print("Не удалось найти слово или описание.")
            return None
    except requests.RequestException as e:
        print(f"Ошибка запроса: {e}")
        return None
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None


# Создаём функцию, которая будет делать саму игру
def word_game():
    print("Добро пожаловать в игру")
    while True:
        # Получаем данные
        word_dict = get_english_words()
        if not word_dict:  # Проверка, что данные получены
            print("Не удалось получить данные. Попробуйте позже.")
            break

        word = word_dict.get("english_words")
        word_definition = word_dict.get("word_definition")

        # Начинаем игру
        print(f"Значение слова - {word_definition}")
        user = input("Что это за слово? ").strip()
        if user.lower() == word.lower():  # Игнорируем регистр
            print("Все верно!")
        else:
            print(f"Ответ неверный, было загадано это слово - {word}")

        # Возможность завершить игру
        play_again = input("Хотите сыграть еще раз? y/n ").strip().lower()
        if play_again != "y":
            print("Спасибо за игру!")
            break


word_game()
