# У нас есть список показаний задолженностей по коммунальным услугам в конце месяца.
# Задолженности могут быть отрицательными — у нас переплата, или положительными, если
# необходимо оплатить по счетам. Напишите функцию amount_payment, которая принимает на вход
# список платежей, суммирует положительные значения и возвращает сумму платежа в конце месяца.


def amount_payment(payment: tuple, sum=0):
    for i in payment:
        if i > 0:
            sum = sum + i
    return sum


print(amount_payment((1, 5, 10, 6, -4, -5)))
