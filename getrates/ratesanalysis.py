# задание 2 содержит:
# чтение файла, сортировка данных из файла по спискам
# перечень функций, решающих задачи для каждого условия

# ...БУДЕТ ПЕРЕНЕСЕНО
# вывод того, что может данный скрипт
# print("""
# Для получения лучшего курса обмена долларов на рубли введите 1;
# Для получения лучшего курса обмена рублей на доллары введите 2;
# Для получения медиан курсов введите 3;
# Для получения средних значений курсов введите 4.
# """)
#
# # ввод данных пользователем
# j = int(input())
# ...
from decimal import Decimal

# создаем класс, который будет делать описанное в комментах ниже и давать функциям подсасывать данные
def proc_file():
    # список для данных полученных из файла
    lines = []
    # открытие файла
    with open('rates.csv', 'r') as file:
        # цикл, читающий файл и построчно добавляющий в список строки с отсечением служебного символа переноса строки
        # и разделяющий строки по знаку разделения ";"
        for line in file:
            lines.append(line.strip().split(";"))

    # удаление нулевого элемента списка (заголовка csv файла)
    lines.pop(0)

    # введение списков для значений курсов
    usdrub = []
    rubusd = []

    # цикл сортирующий значения в соответствующие списки
    for i in range(0, len(lines)):
        usdrub.append(Decimal(lines[i][0]))
        rubusd.append(Decimal(lines[i][1]))

    # упорядочивание списков
    usdrub.sort(), rubusd.sort()
    
    return usdrub, rubusd
    


# функция выводящая лучший курс обмена долларов на рубли
def ur(usdrub):
    print('Лучший курс обмена долларов на рубли:', round(usdrub[-1]), 'RUB за 1 USD')


# функция выводящая лучший курс обмена рублей на доллары
def ru(rubusd):
    print('Лучший курс обмена рублей на доллары:', round(rubusd[-1]), 'USD за 1 RUB')


# функция считающая и выводящая медиану
def med(usdrub, rubusd):
    nu = len(usdrub)
    nr = len(rubusd)
    if nu % 2 == 0:
        median1 = usdrub[nu // 2]
        median2 = usdrub[nu // 2 - 1]
        median = (median1 + median2) / 2
    else:
        median = usdrub[nu // 2]
    print("Медиана курса рубля к доллару:", round(median))

    if nr % 2 == 0:
        median1r = rubusd[nr // 2]
        median2r = rubusd[nr // 2 - 1]
        medianru = (median1r + median2r) / 2
    else:
        medianru = rubusd[nr // 2]
    print("Медиана курса доллара к рублю:", round(medianru))


# функция считающая и выводящая среднее значение
def avg(usdrub, rubusd):
    avgur = sum(usdrub) / len(usdrub)
    avgru = sum(rubusd) / len(rubusd)
    print("Среднее значение курса доллара к рублю:", round(avgur), "\nСреднее значение курса рубля к доллару:", round(avgru))
