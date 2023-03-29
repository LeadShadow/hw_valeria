# datetime -> пакет для роботи з часом в пайтоні

# визначати дату і час
# вираховувати інтервал між двома подіями
# визначати дні тижня, високосного року для будь-якої дати в минулому не раніше року
# datetime.MINYEAR або в майбутньому не пізніше datetime.MAXYEAR
# порівняння дати і часу деяких подій за допомогою операторів зрівняння
# робота з часовими зонами, порівняння подій з врахуванням часових зон і переходу на літній/зимовий час
# перетворення дати/часу в рядок і навпаки

from datetime import datetime

current_datetime = datetime.now()
print(current_datetime.year)
print(current_datetime.month)
print(current_datetime.day)
print(current_datetime.hour)
print(current_datetime.minute)
print(current_datetime.second)
print(current_datetime.microsecond)


print(current_datetime.date())
print(current_datetime.time())


date1 = datetime(year=2008, month=9, day=21)
print(date1.date())


print(date1.weekday())
date2 = datetime(year=2004, month=11, day=28)

diff = date1 - date2
print(diff.total_seconds())

seventh_day_2022 = datetime(year=2022, month=1, day=7, hour=14)
seventh_day_2023 = datetime(year=2023, month=1, day=7, hour=14)

diff = seventh_day_2023 - seventh_day_2022
print(diff.total_seconds())

d = datetime.now()
# next_month.month += 1
next_month = datetime(year=d.year, month=d.month + 1, day=28)
print(next_month.month)
