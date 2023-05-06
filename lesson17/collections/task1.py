"""
Именованные кортежи
Класс collections.namedtuple позволяет создать тип данных, ведущий себя как кортеж с
возможностью присвоить каждому
элементу имя, по которому в дальнейшем можно получить доступ
"""
import collections
from collections import namedtuple

Point = collections.namedtuple('Point', ['x', 'y', 'z'])
p = Point(1, 2, 3)
print(p.x, p.y, p.z)


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

p = Point(1, 2, 3)
print(p.x, p.y, p.z)

Cat = collections.namedtuple('Cats', ['nickname', 'age', 'owner'])

print(Cat.__name__)
cat = Cat('Barsik', 4, 'Oleks')
print(cat.nickname, cat.age, cat.owner)
print(cat)

class Cat:
    def __init__(self, nickname, age, owner):
        self.nickname = nickname
        self.age = age
        self.owner = owner
    def __repr__(self):
        return f'nickname="{self.nickname}", age="{self.age}", owner="{self.owner}"'


cat = Cat('Barsik', 4, 'Oleks')
print(cat.nickname, cat.age, cat.owner)
print(cat)