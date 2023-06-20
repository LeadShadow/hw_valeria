from collections import UserDict, UserList, UserString
import string

class ValueSearchDict(UserDict):
    def __init__(self):
        super().__init__()
        self.data = {}

    def has_in_values(self, value):
        return value in self.data.values()


# self.data = {}
as_dict = ValueSearchDict()
as_dict['a'] = 1
print(as_dict.has_in_values(1))
print(as_dict.has_in_values(2))


class CountableList(UserList):
    def sum(self):
        return sum(map(lambda x: int(x), self.data))


countable = CountableList([1, '2', 3, '4'])
countable.append('5')
print(countable.sum())


class TruncatedString(UserString):
    MAX_LEN = 7
    def truncate(self):
        self.data = self.data[:self.MAX_LEN]


ts = TruncatedString('Hello world!')
ts.truncate()
print(ts)

class NameTooShortError(Exception):
    pass


class NameStartsFromLowError(Exception):
    pass


def enter_name():
    name = input('Enter name: ')
    if len(name) < 3:
        raise NameTooShortError
    if name[0] not in string.ascii_uppercase:
        raise NameStartsFromLowError


while True:
    try:
        name = enter_name()
        break
    except NameStartsFromLowError:
        print('Name should start from big letter. Try again')
    except NameTooShortError:
        print('Name is too short, need more that 3 symbols. Try again')



class Mammal:
    phrase = ''
    def voice(self):
        return self.phrase


class Dog(Mammal):
    phrase = 'Bark!'


class Cat(Mammal):
    phrase = 'Meow!'


class Chupakabra:
    def voice(self):
        return 'WHOOOO!!'


class Recorder:
    def record_animal(self, animal):
        voice = animal.voice()
        print(f'Recorded "{voice}"')


r = Recorder()
cat = Cat()
dog = Dog()
strange_animal = Chupakabra()

r.record_animal(cat)
r.record_animal(dog)
r.record_animal(strange_animal)
