# Вернемся к задаче расчета цены с учетом дисконта и разберем подход с позиции
# каррирования. Создайте функцию discount_price(discount), которая будет определять в себе
# и возвращать функцию расчета реальной цены с учетом скидки.
#
# Вызов функции discount_price(discount) вернет функцию, которая рассчитывает цену на товар
# со скидкой равной discount .
#
# Например:
#
# cost_15 = discount_price(0.15)
# cost_10 = discount_price(0.10)
# cost_05 = discount_price(0.05)
#
# price = 100
# print(cost_15(price))
# print(cost_10(price))
# print(cost_05(price))
# Должен вывести:
#
# 85.0
# 90.0
# 95.0
def better_func(func):
    def inner(discount, price):
        print(f'With a {discount*100}% discount, you get a price of:')
        result = func(discount, price)
        print(f'{result} UAH')
        return result
    return inner
# def better_func(func):
#   def inner(discount):
#     print(f'with a {discount*100}% discount, you get a price of:')
#     result = func(discount)
#     print(f'{result}UAH')
#     return result
#   return inner

@better_func
def discount_price(discount, price):
    result = price - price * discount
    return result


if __name__ == '__main__':
    cost_15 = discount_price(0.15, 100)
    cost_10 = discount_price(0.10, 100)
    cost_05 = discount_price(0.05, 100)