# Необходимо написать функцию реализации следующего игрового алгоритма. На вход функции game
# подается два аргумента: список, состоящий из списков, и начальное значение power - энергия игрока.
# Внутренние списки — это списки с числовым значением энергии, которые может поглотить игрок, если они
# меньше или равные его энергии. После поглощения он двигается по списку дальше и, или поглощает список
# полностью до конца, или, если находит энергию выше собственной, покидает его и переходит к
# следующему списку. В конце обхода всех списков функция должна вернуть общую полученную энергию игрока.

# Пример списка:

# [[1, 1, 5, 10], [10, 2], [1, 1, 1]]
# Для этого списка и начальной энергии равной 1, игрок поглотит из первого списка первые два
# значения и покинет его, встретив значение 5, так как на этот момент будет обладать энергией в 3.
# Второй список пропустит сразу, а третий полностью поглотит и получит окончательную энергию в 6.


list = [[1, 1, 5, 10], [10, 2], [1, 1, 1]]

def game(terra, power=1):
    for terr in terra:
        for energy in terr:
            if energy <= power:
                power += energy
            else:
                break
        print(power)


game(list)