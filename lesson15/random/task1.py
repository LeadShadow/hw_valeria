from random import randint, random, shuffle, choice, choices, sample

print(randint(1, 5))
print(random())


fruits = ['apple', 'banana', 'orange']
shuffle(fruits)
print(fruits)

print(choice(fruits))
print(choices(fruits, k=4))

print(sample(fruits, k=4))



