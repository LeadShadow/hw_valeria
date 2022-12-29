from dot_enter import say_hello
my_tuple = tuple()
another_tuple = ()
a = 10
string = 'string'
not_empty = (1, 2, 3)
print(type(not_empty))
print(type(a))
print(not_empty[0])
print(not_empty[1])
print(not_empty[2])
print(string[0])


for i in not_empty:
    print(i)


empty_dict = {}
empty_dict1 = dict()
print(empty_dict)
print(empty_dict1)

some_dict = {
    'key': 'value',
    1: 'one'
}


not_empty = {'key': 'value'}
not_empty['new_key'] = 'new value'
print(not_empty)
say_hello('user')