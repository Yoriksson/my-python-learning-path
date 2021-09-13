# задание 2 содержит:
# чтение файла, сортировка данных из файла по спискам
# ввод запроса пользователя, перечень условий изходящих из ввода, решение задачи
# для каждого вывода условия

# вывод того, что может данный скрипт
print("""
Для получения лучшего курса обмена долларов на рубли введите 1;
Для получения лучшего курса обмена рублей на доллары введите 2;
Для получения медиан курсов введите 3;
Для получения средних значений курсов введите 4.
""")

# ввод данных пользователем
j = int(input())

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
USDRUB = []
RUBUSD = []

# цикл сортирующий значения в соответствующие списки
for i in range(0, len(lines)):
    USDRUB.append(float(lines[i][0]))
    RUBUSD.append(float(lines[i][1]))

# упорядочивание списков
USDRUB.sort()
RUBUSD.sort()

# перечень условий исходящих из ввода пользователя:
# для ввода 1: Лучший курс обмена долларов на рубли
if j == 1:
    print('Лучший курс обмена долларов на рубли:', USDRUB[-1], 'RUB за 1 USD')
# для ввода 2: Лучший курс обмена рублей на доллары
elif j == 2:
    print('Лучший курс обмена рублей на доллары:', RUBUSD[-1], 'USD за 1 RUB')
# для ввода 3: медианы курсов
elif j == 3:
    Nu = len(USDRUB)
    Nr = len(RUBUSD)
    if Nu % 2 == 0:
        median1 = USDRUB[Nu//2]
        median2 = USDRUB[Nu//2 - 1]
        median = (median1 + median2)/2
    else:
        median = USDRUB[Nu//2]
    print("Медиана курса рубля к доллару:", median)

    if Nr % 2 == 0:
        median1r = RUBUSD[Nr//2]
        median2r = RUBUSD[Nr//2 - 1]
        medianru = (median1r + median2r)/2
    else:
        medianru = RUBUSD[Nr//2]
    print("Медиана курса доллара к рублю:", medianru)
# для ввода 4: среднее значение курсов
elif j == 4:
    print("Среднее значение курса доллара к рублю:", sum(USDRUB)/len(USDRUB))
    print("Среднее значение курса рубля к доллару:", sum(RUBUSD)/len(RUBUSD))
# если ввод не подходит ни под одно из условий
else:
    print("Это не предусмотрено заданием, Слава Арстотцке!")
