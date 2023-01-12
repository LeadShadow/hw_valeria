# user_input = input('Input list: ')
#
# print(user_input.split(' '))

# словники

chars = {
    'a': 1,
    'b': 2
}
# повернення значення елементу и видаляє пару ключ-значення (pop)
b_num = chars.pop('b')  # 2
print(chars)  # {'a': 1}
print(b_num)  # 2

# розширює словник значеннями з іншого словника (update)
chars.update({'c': 3})
print(chars)

# очищує словник не створюючи нового (clear)
chars.clear()
print(chars)

# повертає копію словника
chars = {
    'a': 1,
    'b': 2
}
chars_copy = chars.copy()
print(chars == chars_copy)

# print(chars['b']) -> 2 -> print(chars.get('b'))
print(chars['a'])
print(chars.get('g', 5))

# ітерування
numbers = {
    1: 'one',
    2: 'two',
    3: 'three'
}

for k, v in numbers.items():
    print(k, v)

# множини

a = set()
print(a)

a = set('hello')  # {}
print(a)

b = {1, 2, 3, 4}
print(b)
print(b)

numbers = {1, 2, 3, 1, 2, 3}
print(numbers)


# add -> додає елемент в множину
numbers.add(5)
print(numbers)

# remove -> удаляє елемент з множини і викликає виняток якшо такого елементу немає
numbers.remove(2)
print(numbers)

# discard -> удаляє елемент з множини і не викликає виняток якшо такого елементу немає
numbers.discard(6)
print(numbers)


a = set('hello')
print(a)

b = set('hi there!')
print(b)

# & пересічення елементів двох множин(and)
print(a & b)

# ^ знайдемо всі елементи з двох множин окрім спільних (xor)
print(a ^ b)

# | об'єднання множин, або просто всі елементи двох множин
print(a | b)


# кортежі
points = {
    (0, 0): 'O',
    (1, 1): 'A',
    (2, 2): 'B'
}
my_tuple = (1, 2, 3, 4, 5)

print(my_tuple[3])
