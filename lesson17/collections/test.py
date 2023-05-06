# Іменований кортеж
import collections
person = ('Sasha', 'Samus', 18, 'Keletskya', '98')


Person = collections.namedtuple('Person', ['name', 'last_name', 'age', 'place', 'index'])

person = Person('Sasha', 'Samus', 18, 'Keletskya', '98')

print(person.name)
print(person.last_name)
print(person[3])

