from random import randint


# number = randint(0, 10)
# print(number)


def game(n: int):
    count = 0
    goal = randint(0, n)
    while True:
        answer = int(input(f'Вгадайте задумане число від 0 до {n}: '))
        count += 1
        if answer > goal:
            print('Ваше число більше задуманного')
        elif answer < goal:
            print('Ваше число менше задуманного')
        else:
            print(f'Вітаю! Ви вгадали число {goal} за {count} крок/ів')
            break


if __name__ == "__main__":
    game(30)
