# 101010100101010101
from decimal import Decimal, getcontext

print(round(0.1 + 0.2, 2) == 0.3)
print(0.1 + 0.2)

getcontext().prec = 6
print(Decimal(1) / Decimal(7))


getcontext().prec = 28
print(Decimal(1) / Decimal(7))


print(Decimal(0.1) + Decimal(0.2) == Decimal(0.3))

print(round(10.151010, 2))