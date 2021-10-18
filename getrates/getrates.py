# Данный скрипт является первой частью задания, он получает данные о курсе валют и записывает их в файл в формате csv

import requests
import json
import time
from tqdm import tqdm
from datetime import datetime


class Indicator:
    USDRUB = None
    RUBUSD = None
    datetime_moment = None

    def __init__(self, USDRUB: float, RUBUSD: float):
        self.USDRUB = USDRUB
        self.RUBUSD = RUBUSD
        self.datetime_moment = datetime.now()

    def get_datetime_format(self):
        return self.datetime_moment.strftime("%c")


class IndicatorFabric:

    def compile(self, USDRUB):
        RUBUSD = 1/USDRUB
        indicator = Indicator(USDRUB, RUBUSD)
        return indicator

    def compile_lots(self, list_of_USDRUB):
        list_of_indicator = []
        for i in list_of_USDRUB:
            list_of_indicator.append(self.compile(i))
        return list_of_indicator

class IndicatorManager:

    list_of_indicator = []
    url = None
    filename = None

    def __init__(self, url, filename):
        self.url = url
        self.filename = filename

    def get_from_url(self):
        response = requests.get(self.url)
        data = json.loads(response.content)
        USDRUB = data['Valute']['USD']['Value']
        ifg = IndicatorFabric()
        indicator = ifg.compile(USDRUB)
        print(indicator.USDRUB, indicator.RUBUSD, indicator.get_datetime_format())
        self.list_of_indicator.append(indicator)


    def get_all(self) -> Indicator:
        pass

    def get_filer(self, time) -> Indicator:
        pass



if __name__ == "__main__":
    test = IndicatorManager(url='https://www.cbr-xml-daily.ru/daily_json.js', filename='file.csv')
    test.get_from_url()

#
# def ratesget():
#     # Очистка файла перед началом цикла, для актуальности информации
#     with open('rates.csv', 'w') as file:
#         file.write("USDRUB;RUBUSD\n")
#
#     # Переменная для цикла
#     i = 0
#
#     # Цикл получения актуальных данных и записи в файл в формате csv, по условию задачи работает с интервалом в 5 минут
#     # и производит 288 запросов за сутки, после чего завершается(для теста сокращено до 11 обращений)
#     for i in tqdm(range(10)):
#         # Получение данных от api
#         response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
#
#         # Конвертация данных в формат python
#         data = json.loads(response.content)
#
#         # Присвоение переменной значения курса
#         USDRUB = data['Valute']['USD']['Value']
#
#         # Нахождение обратного курса
#         RUBUSD = 1 / USDRUB
#
#         # Добавление новой строчки с текущими курсами в файл
#         with open('rates.csv', 'a') as file:
#             file.write(str(USDRUB) + ";" + str(RUBUSD) + '\n')
#
#         # Пауза 300 секунд (5 минут) по условию задачи(для теста сокращено до 5 секунд)
#         time.sleep(5)
