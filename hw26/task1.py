# Завдання: Реалізація ітератора
# Опис: Створіть клас MyRange, який поводиться подібно до вбудованої функції range(),
# але використовує магічний метод __iter__ для реалізації ітератора. Клас MyRange
# повинен дозволяти ітерувати послідовність цілих чисел в заданому діапазоні.
# range(10) -> 0123456789
# range(1, 10) -> 123456789
# range(1, 10, 2) -> 1, 3, 5, 7, 9
class MyRange:
    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        current = self.start
        while current < self.end:
            yield current
            current += self.step


my_range = MyRange(1, 10, 2)
for num in my_range:
    print(num)


my_range1 = MyRange(10)
for num in my_range1:
    print(num)

