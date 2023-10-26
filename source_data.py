# INFORMATION
# данные в таблицу в базе вносятся через SQLiteStudion:
# создаётся пустой файл, затем таблица с нужными полями и далее заполняется вручную

# Импортируем функции для случайного выбора
from random import choice
# импорт библиотеки работы с базой данных SQLite
import sqlite3

# Создаём переменные с которыми будем работать
# полный словарь
quest_dict = {}
# Вложенный словарь с вопросом
q_dict = {}
# Кортеж со значениями
t_val = ()
# кортеж с ключами
t_key = ('question', 'correct_answer', 'raiting',  'A', 'B', 'C', 'D')

# скрипт для вывборки из базы данных нужных эллементов
script = """SELECT id, question, correct_answer, raiting, a, b, c, d
  FROM questions
  order by id"""

# Подключаем базу данных
source_db = sqlite3.connect("Quiz.db")
# создаём структуры для получения выборки
cursor = source_db.cursor()
# выполняем скрипт
cursor.execute(script)
# загружаем полученные данные в переменную
y = cursor.fetchall()
# Создаём финальный словарь из полученных значений
for i in range(len(y)):
    t_val = y[i][1:]  # срез кортежа без нулевого элемента
    q_dict = {t_key[j]: t_val[j] for j, _ in enumerate(t_val)}  # собираем словарь одного вопроса
    quest_dict["question" + str(y[i][0])] = q_dict  # добавляем каждый вопрос в общий словарь

# print(quest_dict)  # проверка результата


# случайно выбираем один из вопросов из общего словаря
def take_question():
    return choice(list(quest_dict.items()))
