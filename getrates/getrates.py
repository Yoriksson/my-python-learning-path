# Данный скрипт является первой частью задания, он получает данные о курсе валют и записывает их в файл в формате csv

import requests
import json
import time


def ratesget():
    # Очистка файла перед началом цикла, для актуальности информации
    with open('rates.csv', 'w') as file:
        file.write("USDRUB;RUBUSD\n")

    # Переменная для цикла
    i = 0

    # Цикл получения актуальных данных и записи в файл в формате csv, по условию задачи работает с интервалом в 5 минут
    # и производит 288 запросов за сутки, после чего завершается(для теста сокращено до 11 обращений)
    for i in range(10):
        # Получение данных от api
        response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')

        # Конвертация данных в формат python
        data = json.loads(response.content)

        # Присвоение переменной значения курса
        USDRUB = data['Valute']['USD']['Value']

        # Нахождение обратного курса
        RUBUSD = 1 / USDRUB

        # Добавление новой строчки с текущими курсами в файл
        with open('rates.csv', 'a') as file:
            file.write(str(USDRUB) + ";" + str(RUBUSD) + '\n')

        # Пауза 300 секунд (5 минут) по условию задачи(для теста сокращено до 5 секунд)
        time.sleep(5)
