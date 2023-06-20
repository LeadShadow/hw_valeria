# Для предыдущей задачи реализуйте в классе Animal метод change_weight, который должен
# менять вес животного.
#
# Вызовите функцию change_weight(12) для объекта animal и измените значение изначального
# веса с 10 на 12 единиц.
class Animal():
  nickname = ''
  weight = 10
  def change_weight(self, new_weight):
    self.weight = new_weight

animal = Animal()
animal.change_weight(12)
print(animal.weight)