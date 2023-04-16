import random

d = {
    1: 'Орел',
    2: 'Решка'
}

def game():
    count_O = 0
    count_P = 0
    sequence = []
    count = 0
    while count_P < 3 and count_O < 3:
        number = random.randint(1, 2)
        if number == 1:
            count_O += 1
            count_P = 0
        else:
            count_O = 0
            count_P += 1
        count += 1
        sequence.append(d[number])
    print(f'Отримана послідовність: {sequence}')
    if count_O == 3:
        print('Випало три орла підряд')
    else:
        print('Випало три решки підряд')
    print(f'Кількість спроб: {count}')


if __name__ == "__main__":
    game()