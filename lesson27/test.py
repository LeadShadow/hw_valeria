# +38093-731(60)-48) -> 380937316048
from collections import UserDict


class ListedValuesDict(UserDict):
    def __setitem__(self, key, value):
        if key in self.data:
            self.data[key].append(value)
        else:
            self.data[key] = [value]
# {'key': [1, 2, 3, 4]}
    def __getitem__(self, key):
        result = str(self.data[key][0])
        for value in self.data[key][1:]:
            result += ', '+ str(value)
        return result  # '1, 2, 3, 4'


l_dict = ListedValuesDict()
l_dict[1] = 1
l_dict[1] = 2
l_dict[1] = 3
l_dict[1] = 4
print(l_dict[1])

# Функтори
class Adder:
    def __init__(self, add_value):
        self.add_value = add_value

    def __call__(self, value):
        return self.add_value + value


two_adder = Adder(2)
print(two_adder(3))


class Error:
    def __init__(self, func) -> None:
        self.func = func

    def __call__(self, x, y):
        try:
            print(self.func(x, y))
        except TypeError:
            print('Error give me two numbers')


@Error
def sum_func(x, y):
    return x + y


sum_func('4', 5)


class Session:
    def __init__(self, addr, port=8080):
        self.connected = False
        self.addr = addr
        self.port = port
        # 127.0.0.0:8000  localhost:port

    def __enter__(self):
        self.connected = True
        print(f'connected to {self.addr}:{self.port}')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connected = False
        if exc_type is not None:
            print('Some Error!')
        else:
            print('GoodBye!')


localhost = Session('localhost')
with localhost as session:
    print(session is localhost)
    print(localhost.connected)

print(localhost.connected)
