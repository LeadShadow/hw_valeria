# Создайте класс NumberString, наследуйте его от класса UserString, определите для него метод
# number_count(self), который будет считать количество цифр в строке.
from collections import UserString


class NumberString(UserString):
    def number_count(self):
