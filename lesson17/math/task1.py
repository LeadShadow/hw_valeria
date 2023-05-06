import math

print(math.sin(math.pi / 4))
print(math.degrees(math.pi / 4))


x = float(input('x = '))
y = float(input('y = '))

a = math.log(math.pow(y, math.sqrt(math.fabs(x)))) * (math.sin(x) + math.exp(x + y))
print(a)

print(0.1 + 0.2 == 0.3)
r = math.isclose(0.1 + 0.2, 0.3)
print(r)


print(math.isclose(0.1, 0.100000000000000009))

print(abs(0.1 - 0.1001) < 0.00001)
