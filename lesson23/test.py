from pathlib import Path

class User:
    name = 'UserName'
    age = 15


user1 = User()
print(user1.name)
print(user1.age)

user2 = User()
user2.name = 'Tom'
user2.age = 18
print(user2.name)
print(user2.age)


class User:
    name = 'UserName'
    age = 15

    def say_name(self):
        print(f'Hi I am {self.name} and I am {self.age} years old')

    def set_age(self, age):
        self.age = age



bob = User()
bob.name = 'Bob'

bob.say_name()

class Object:
    public = 'I am public'
    _close = 'I am close but I\'m visible'
    __private = 'I am private'


ob = Object()
print(ob.public)
print(ob._close)
print(ob._Object__private)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        return f'Hi {self.name}'


p = Person('Sasha', 18)
print(p.greeting())


class Human:
    name = ''
    def voice(self):
        print(f'Hello! My name is {self.name}')


class Developer(Human):
    field_description = 'My programming language'
    language = ''
    def make_some_code(self):
        return f'{self.field_description} is {self.language}'


class PythonDeveloper(Developer):
    language = 'Python'


class JSDeveloper(Developer):
    language = 'JS'


p_dev = PythonDeveloper()
p_dev.name = 'Sasha'
p_dev.voice()
print(p_dev.make_some_code())

js_dev = JSDeveloper()
print(js_dev.make_some_code())


# 1клас - 10 методів, 2клас(1) -> 5методів з 1 класу

class People:
    def like_drive_on_car(self):
        return f'People like drive on a car'

    def like_drive_on_bike(self):
        return f'People like drive on a bike'


class WhoLikeCar:
    def __init__(self, peop):
        self.peop = peop

    def print_message(self):
        print(self.peop.like_drive_on_car())


people = People()
wlc = WhoLikeCar(people)
wlc.print_message()


class A:
    x = 'I am A class'


class B:
    x = 'I am B class'
    y = 'I exists only in B class'


class C(A, B):
    c = 'I exists only in C class'


c = C()
print(c.c)
print(c.y)
print(c.x)

