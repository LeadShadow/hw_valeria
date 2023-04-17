"""
Необходимость использования. Настройка точности
"""
from decimal import Decimal, getcontext
getcontext().prec = 6
print(Decimal(1) / Decimal(7))


getcontext().prec = 28
print(Decimal(1) / Decimal(7))


getcontext().prec = 20
print(float(Decimal(0.1) + Decimal(0.2)) == 0.3)

f = 0.2 + 0.1 + 0.3 - 0.5
print(f)

df = Decimal('0.1') + Decimal('0.2') + Decimal(0.3) - Decimal(0.5)
print(df)