# Написати функцію is_prime, яка приймає 1 аргумент - число від 0 до 1000,
# і повертає True, якщо воно просте, і False - інакше. -> прості числа це числа які
# діляться лише на 1 і на самого себе =)

# 1, 2, 3, 4, 5, 6, 7, 8, 9
def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


print(is_prime(7))

