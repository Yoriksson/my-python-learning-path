# проверка работоспособности сего творения

# импорт самопальных модулей
import getrates
import ratesanalysis

# вызов функций самопальных модулей
# getrates.ratesget()

date_from_file = ratesanalysis.proc_file()
ratesanalysis.avg(*date_from_file)
ratesanalysis.ru(date_from_file[1])
ratesanalysis.ur(date_from_file[0])
ratesanalysis.med(*date_from_file)

# вывод на момент теста:
# Среднее значение курса доллара к рублю: 72.65333333333334
# Среднее значение курса рубля к доллару: 0.013764143752893344
# Лучший курс обмена рублей на доллары: 0.013888888888999999 USD за 1 RUB
# Лучший курс обмена долларов на рубли: 72.76 RUB за 1 USD
# Медиана курса рубля к доллару: 72.76
# Медиана курса доллара к рублю: 0.013743815283122594