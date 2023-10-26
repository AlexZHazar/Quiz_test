# INFORMATION
# необходимо подключить библиотеку PySimpleGUI c pysimplegui-exemaker
# для создания отдельного exe файла необходимо в терминале выполнить команду:
# python -m pysimplegui-exemaker.pysimplegui-exemaker
# для работы необходимо, иметь корректный файл базы данных рядом в исполняемым файлом программы

# Импортируем графическую библиотеку
import PySimpleGUI as sg
# Импортируем файл со словарём
import source_data as sd


# Основная функция по прорисовке окна
def the_gui():

    # Инициализация переменных
    corr_answ = ''
    # question_rating = 0
    status = 1

    # Тема окна
    sg.theme('Dark Blue 4')

    # Построчное расположение элементов
    layout = [
        [sg.Text(' '*200,),
         sg.Button('?', key='-POPUP-', border_width=0, button_color=('black', sg.theme_background_color()))],
        # ^ Кнопка дополнительной информации
        [sg.Button('  Следующий вопрос  ', key='-NQ-')],
        # ^ кнопка для перехода к следующему вопросу
        [sg.Text('Вопрос:'), sg.Text('', key='-Q-'), sg.Text('       Сложность:'), sg.Text('', key='-R-')],
        [sg.Text('')],
        # ^ Текстовый вывод информации

        [sg.Radio('', 'Radio1', key='-A-', disabled=True)],
        [sg.Radio('', 'Radio1', key='-B-', disabled=True)],
        [sg.Radio('', 'Radio1', key='-C-', disabled=True)],
        [sg.Radio('', 'Radio1', key='-D-', disabled=True)],
        # ^ Группа выбора ответа

        [sg.Text('')],
        [sg.Button('  Ответ:  ', key='-CA-', disabled=True)],
        # ^ Кнопка отображения результата
        [sg.Text('')],
        [sg.Text('Результат:'), sg.Text(key='-RESULT-')],
        [sg.Text('')],
        # ^ Отображение корректности данного ответа
    ]

    # Создание окна
    window = sg.Window('Quiz', layout, finalize=True)

    # --------------------- EVENT LOOP ---------------------
    while True:

        # Бесконечное чтение элементов окна
        event, values = window.read(timeout=100)  #TODO: set timeout 1000 or 100

        # Условия закрытия окна
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        # Начало процесса спросить-ответить
        elif event == '-NQ-':
            # ^ Проверка на переход к следующему вопросу
            window['-RESULT-'].update("")
            # ^ Поле для вывода результат (коррект/инкоррект) очищается
            status = 1
            # ^ Обозначение флага блокировки элементов
            qlist = sd.take_question()
            # ^ Записываем в словарь пришедшие элементы из sorce_data (1 вопрос)
            q = qlist[1]
            # ^ убираем 0й элемент

            # Читаем по ключам элементы пришедшего словаря и блокируем/разблокируем кнопки нового вопроса/ответа
            for key, value in q.items():
                if key == 'question':
                    window['-Q-'].update(value)
                elif key == 'correct_answer':
                    corr_answ = value
                elif key == 'raiting':
                    # question_rating = value
                    window['-R-'].update(value)
                else:
                    event_key = '-'+key+'-'
                    window[event_key].update(disabled=False)
                    window[event_key].update(False)
                    window[event_key].update(text=value)

        # нажатие кнопки проверки
        elif event == '-CA-':
            # Апдейтим кнопки к изначальному состоянию для продолжения викторины
            window['-NQ-'].update(disabled=False)
            window['-CA-'].update(disabled=True)
            window['-A-'].update(disabled=True)
            window['-B-'].update(disabled=True)
            window['-C-'].update(disabled=True)
            window['-D-'].update(disabled=True)

            # Сверяем отмеченный результат с правильным ответом
            for key, value in values.items():
                if value:
                    if key == '-'+corr_answ+'-':
                        window['-RESULT-'].update("  Верно!  ")
                    else:
                        window['-RESULT-'].update("  Неверно!  ")

        # Проверяем выбрал ли пользователь ответ
        elif event == '__TIMEOUT__':
            for key, value in values.items():
                if status == 1 and value:
                    window['-NQ-'].update(disabled=True)
                    window['-CA-'].update(disabled=False)
                    status = 0

        # окно информации
        elif event == '-POPUP-':
            sg.popup("""
_______Quize for test_______
      Alexandr Zhirnov
""")

    window.close()


################################################################

# Начало кода XD
if __name__ == '__main__':
    the_gui()
