# Все вы, возможно, сталкивались с ребусами "Найди слово". Они существуют как
# текстовые варианты, так и программы для мобильных приложений. Напомним кратко суть ребуса.
# В большом квадрате с набором бук необходимо найти слово по горизонтали и, иногда, по вертикали.
#
# game
# Реализуйте функцию solve_riddle(riddle, word_length, start_letter, reverse=False) для
# нахождения искомого слова в строке ребуса.
#
# Параметры функции:
#
# riddle - строка с зашифрованным словом.
# word_length - длина зашифрованного слова.
# start_letter - буква, с которой начинается слово (подразумевается, что до начала слова буква
# не встречается в строке).
# reverse - указывает, в каком порядке записано слово. По умолчанию — в прямом. Для значения
# True слово зашифровано в обратном порядке, к примеру, в строке mi1rewopret зашифровано слово
# power.
# Функция должна возвращать первое найденное искомое слово. Если слово не найдено, вернуть
# пустую строку.


def solve_riddle(riddle: str, word_length, start_letter, reverse=False):
    if reverse:
        riddle = riddle[::-1]
    pos = riddle.find(start_letter, 0, len(riddle) - word_length)
    return '' if pos == -1 else riddle[pos: pos + word_length]


print(solve_riddle('mi1rewopret', 5, 'p', reverse=True))

for i in range(16):
    print('{:^10} {:^10} {:^10}'.format(i, i, i))
# dwadappledaw
