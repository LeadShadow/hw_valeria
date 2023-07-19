class Iterable:
    MAX_VALUE = 10
    def __init__(self):
        self.current_value = 0

    def __next__(self):
        if self.current_value < self.MAX_VALUE:
            self.current_value += 1
            return self.current_value
        raise StopIteration


class CustomIterator:
    def __iter__(self):
        return Iterable()


c = CustomIterator()
for i in c:
    print(i)

print('------------------------')
for i in range(1, 11):
    print(i)


class Secret:
    public_field = 'This is public'
    _private_field = 'avoid using this'
    __real_secret = 'I am hidden'


s = Secret()
print(s.public_field)
print(s._private_field)
print(s._Secret__real_secret)


class PositiveNumber:
    def __init__(self):
        self.__value = None

    @property
    def value(self):
        if self.__value is None:
            return None
        return self.__value

    @value.setter
    def value(self, new_value):
        if new_value > 0:
            self.__value = new_value
        else:
            print('Need > 0')


p = PositiveNumber()
# p.value = 1
# print(p.value)  # 1
p.value = -1
print(p.value)
p._PositiveNumber__value = -1
print(p.value)

