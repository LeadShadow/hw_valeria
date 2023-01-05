my_list = []
my_list1 = list()

print(my_list)
print(my_list1)

not_empty = [1, 2, 'user', (1, 2, 3)]
print(not_empty)
some_list = ['a', 'b', 'c']
first_letter = some_list[0]
second_letter = some_list[1]
third_letter = some_list[2]
print(first_letter, second_letter, third_letter)

first_letter = some_list[-3]
second_letter = some_list[-2]
third_letter = some_list[-1]
print(third_letter, second_letter, first_letter)

some_list[1] = 'z'
print(some_list)
some_str = 'This is awesome string'
first_five = some_str[0:5]
print(first_five)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_numbers = numbers[0:10:2]
even_numbers = numbers[1:10:2]
three_numbers = numbers[2:10:3]
print(odd_numbers, even_numbers, three_numbers)

odd_numbers = numbers[::2]
even_numbers = numbers[1::2]
three_numbers = numbers[2:10:3]

numbers_copy = numbers[:]
numbers = [0, 1, 2, 3]
first_three = numbers[0:3]
print(first_three)
symbols = ['a', 'b']
symbols.append('c')
print(symbols)
# symbols.clear()
# print(symbols)
symbols.remove(symbols[1])
print(symbols)

symbols.pop(-1)
print(symbols)
symbols.extend(numbers)
print(symbols)

symbols.insert(1, 'b')
symbols.insert(1, 'b')
print(symbols)

index = symbols.index('b')
print(index)

count = symbols.count('b')
print(count)
chars = ['X', 'H', 'A', 'z', 'x', 'c', 'f', 'g', 'a', 'b']
chars.sort()
chars.reverse()
print(chars)

chars_copy = chars.copy()
print(chars_copy)
print(chars_copy == chars)
print(chars_copy[::-1])
