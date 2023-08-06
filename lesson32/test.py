import pickle
import json
expenses = {
    'hotel': 700,
    'breakfast': 100,
    'taxi': 150,
    'lunch': 150
}


file_name = 'expenses.txt'
with open(file_name, 'w') as file:
    for key, value in expenses.items():
        file.write(f'{key}|{value}\n')


expenses_result = {}
with open(file_name, 'r') as file:
    for line in file:
        key, value = line.split('|')
        expenses_result[key] = int(value)

print(expenses_result == expenses)


some_data = {
    3.5: 'tuple',
    2: [1, 2, 3],
    'a': {'key': 'value'},
    'b': (1, 2, 3)
}

byte_string = pickle.dumps(some_data)
print(byte_string)
unpacked = pickle.loads(byte_string)
print(unpacked)


file_name = 'data.bin'  # .bin, .dat

with open(file_name, 'wb') as file:
    pickle.dump(some_data, file)  # серіалізація


with open(file_name, 'rb') as file:
    unpacked = pickle.load(file)

print(unpacked == some_data)
print(unpacked is some_data)


class Human:
    def __init__(self, name):
        self.name = name


sasha = Human('Sasha')
encoded_sasha = pickle.dumps(sasha)

decoded_sasha = pickle.loads(encoded_sasha)
print(sasha.name == decoded_sasha.name)


class Person(Human):
    def __init__(self, name, surname, work):
        self.name = name
        self.surname = surname
        self.work = work

    def __str__(self):
        return f'{self.name} - {self.surname}, place of work: {self.work}'


sasha = Person('Sasha', 'Samus', 'IT')

file_name = 'data.bin'  # .bin, .dat

with open(file_name, 'wb') as file:
    pickle.dump(sasha, file)


with open(file_name, 'rb') as file:
    unpacked = pickle.load(file)


print(unpacked)
# None -> nan -> js
# 3 -> '3'
# '3' -> 3


with open('test.json', 'w') as file:
    json.dump(some_data, file)


with open('test.json', 'r') as file:
    unpacked = json.load(file)


print(unpacked)
