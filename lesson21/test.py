# функція як об'єкт першого класу


# 1 можемо створювати змінні і записувати в них функцію
def func(x, y):
    return x + y


func_result = func
result = func_result(10, 10)
print(func(10, 10))

# 2 можемо передавати функцію як аргументи для інших функцій
def sum_func(x, y):
    return x + y

def sub_func(x, y):
    return x - y

def tricky_func(x, y, func):
    return func(x, y)


sum_result = tricky_func(2, 3, sum_func)
print(sum_result)
sub_result = tricky_func(2, 3, sub_func)
print(sub_result)

# 3 можемо повертати з функції інші функції

def sum_func(x, y):
    return x + y

def sub_func(x, y):
    return x - y

def get_operator(operator):
    if operator == '+':
        return sum_func
    elif operator == '-':
        return sub_func
    else:
        print('Unknown operator')


sum_action = get_operator('+')
print(sum_action(2, 3))


X = 15
def func(x):
    X = x
    print(X)

def proc():
    print(X)

proc()
func(5)
print(X)

def func1(x):
    def func2(list1):
        max_num = max(list1)



# Замикання
def adder(value):
    def inner(x):
        def wrapper(y):
            return x + value + y
        return wrapper
    return inner

two_adder = adder(2)
two_inner = two_adder(10)
print(two_inner(10))

# Carrying

# Не рекомендується
# def sum_func(x, y):
#     return x + y
#
# def sub_func(x, y):
#     return x - y
#
# def get_operator(operator):
#     if operator == '+':
#         return sum_func
#     elif operator == '-':
#         return sub_func
#     else:
#         print('Unknown operator')

def sum_func(x, y):
    return x + y

def sub_func(x, y):
    return x - y

OPERATIONS = {
    '-': sub_func,
    '+': sum_func
}

def get_handler(operator):
    return OPERATIONS.get(operator, 'Unknown operator')

handler = get_handler('+')
print(handler(2, 3))



def logged_func(func):
    def inner(x, y):
        print(f'called with {x}, {y}')
        result = func(x, y)
        print(f'result: {result}')
        return result
    return inner


@logged_func
def complicated(x, y):
    return x / y

print(complicated(10, 10))