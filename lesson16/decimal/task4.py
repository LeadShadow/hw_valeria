"""
Сравнение двух десятичных чисел
Значение 0 указывает, что оба числа равны,
значение 1 указывает, что первое число больше второго числа,
а значение -1 указывает, что первое число меньше второго.
"""
from decimal import Decimal


print(Decimal('1.2').compare(Decimal('1.1')))
print(Decimal('1.0').compare(Decimal('1.1')))
print(Decimal('1.0').compare(Decimal('1.0')))
