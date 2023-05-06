sq = []

for i in range(1, 6):
    sq.append(i ** 2)


print(sq)


numbers = [i for i in range(1, 6)]
print(numbers)

sq1 = [i ** 2 for i in range(1, 6)]
print(sq1)
print(sq == sq1)


# set
numbers = [1, 4, 1, 3, 2, 5, 2, 6]
sq = {i ** 2 for i in numbers}
print(sq)


# dict
sq = {i: i ** 2 for i in numbers}
print(sq)
