# В прошлую задачу добавим класс Owner — владельца собаки. У класса есть три атрибута:
# имя — name, возраст — age и адрес — address. Также необходимо реализовать метод info,
# который возвращает словарь с ключами 'name', 'age' и 'address', и значениями равными
# соответствующим свойствам экземпляра класса.
#
# Реализовать для класса Dog атрибут owner, который будет экземпляром класса Owner.
# Добавить в класс Dog метод who_is_owner, который возвращает результат вызова метода
# info у экземпляра класса Owner, т.е. словарь с ключами 'name', 'age' и 'address' владельца.
class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Owner:
    def __init__(self, ):
        pass

    def info(self):
        pass


