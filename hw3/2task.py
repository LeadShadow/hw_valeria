# Написати функцію аритметичного, що приймає 3 аргументи: перші 2 - числа,
# третій - операція, яка повинна бути проведена над ними.
# Якщо третій аргумент +, скласти їх; якщо -, то відняти; * - помножити; /
# - Розділити (перше на друге). В інших випадках повернути рядок
# "Невідома операція".


def arifmetic(a: int, b: int, op) -> None:
    if op == "+":
        print(a+b)
    elif op == "-":
        print(a-b)
    elif op == "*":
        print(a*b)
    elif op == "/":
        print(a/b)
    else:
        print('Невідома операція')

arifmetic(5, 10, '+')
