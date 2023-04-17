# Создание Decimal из вещественных чисел

from decimal import Decimal

num1 = 1.38
num2 = 1.45

f = Decimal(num1)
s = Decimal(num2)

print(f, s)

f = Decimal(str(num1))
s = Decimal(str(num2))
print(f, s)