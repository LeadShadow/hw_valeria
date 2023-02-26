# Приклад 2
# """ Створіть файл nums.txt, що містить кілька чисел, записаних через пропуск.
# Напишіть програму, яка підраховує і виводить на екран загальну суму чисел, що
# зберігаються в цьому файлі.

from random import randint


def num_input():
    file = open('nums.txt', 'w', encoding='utf-8')
    for _ in range(7):
        i = str(randint(0, 10)) + ' '
        file.write(i)
    file.close()


def sum_nums():
    sum_num = 0
    with open('nums.txt', 'r', encoding='utf-8') as fh:
        file = fh.read().split()
        for i in file:
            i = int(i)
            sum_num += i
    return sum_num


if __name__ == "__main__":
    num_input()
    print(sum_nums())