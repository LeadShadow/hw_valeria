class Secret:
    public_field = 'This is public'
    _private_field = 'avoid using this'
    __real_secret = 'I am hidden'


s = Secret()
print(s.public_field)
print(s._private_field)
print(s._Secret__real_secret)


class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        print('Getting name')
        return self.__name

    @name.setter
    def name(self, value):
        print('Setting value')
        self.__name = value

    @property
    def age(self):
        print('Getting age')
        return self.__age

    @age.setter
    def age(self, value):
        print('Setting age')
        if value < 0:
            raise ValueError('Age cannot be negative')
        self.__age = value


person = Person('Sasha', 18)

print(person.name)  # виклик getter-a

person.name = 'Mike'  # виклик setter-a

print(person.name)  # виклик getter-a

person.age = -5
