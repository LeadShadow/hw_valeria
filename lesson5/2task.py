# Написати функцію useless(list) де параметр list буде випадковий список
# Знайти в цьому списку максимальне значення і розділити його на довжину списка
# my_list = [1, 2, 3]
# len(my_list) -> 3
def useless(my_list: list) -> int:
    max_ = 0
    for i in my_list:
        if i > max_:
            max_ = i
    return max_ // len(my_list)


print(useless([1, 3, 5, 9, 11, 15, 4, 6]))
