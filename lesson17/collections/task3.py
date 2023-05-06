"""
defaultdict
collections.defaultdict ничем не отличается от обычного словаря за исключением того, что
по умолчанию всегда вызывается
функция, возвращающая значение:
"""
from collections import defaultdict

data_d = defaultdict(list)

data_d[0].append(10)
print(data_d)
data_d[0].append(1)
print(data_d)


colors = [('yellow', 1), ('blue', 3), ('yellow', 5), ('blue', 10), ('red', 13)]

colord_d = defaultdict(list)
for k, v in colors:
    colord_d[k].append(v)
print(colord_d)