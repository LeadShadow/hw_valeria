# Разработайте функцию get_days_from_today(date), которая будет возвращать
# количество дней от текущей даты, где параметр date — это строка формата
# '2020-10-09' (год-месяц-день).
#
# Подсказки:
#
# Параметр date разбить на год, месяц и день можно, используя метод строк split.
# datetime принимает аргументы типа int, используйте преобразование типов.
# игнорируйте часы, минуты и секунды для вашей даты, важны полные дни.
# количество дней вы можете получить вычитанием из текущей даты, заданной в date
# (без времени).
# Например: Если текущая дата — 5 мая 2021, то вызов get_days_from_today("2021-10-09")
# вернет нам -157.
from datetime import datetime


def get_days_from_today(date):
    date = date.split('-')
    a, b, c = int(date[0]), int(date[1]), int(date[2])
    another_date = datetime(year=a, month=b, day=c)
    current_datetime = datetime.now()
    difference = current_datetime - another_date
    return difference


print(get_days_from_today("2021-10-09"))
