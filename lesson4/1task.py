# У нас подається кортеж з чисел, знайти факторіал найбільшого з значень кортежу
from factorial import factorial
my_tuple = (1, 2, 3, 4, 5)


def find_max(tuple1):
    max_ = 0
    for i in tuple1:
        if i > max_:
            max_ = i
    return max_

# find_max(my_tuple) -> 5
# factorial(find_max(my_tuple)) -> factorial(5)


if __name__ == "__main__":
    print(factorial(find_max(my_tuple)))
