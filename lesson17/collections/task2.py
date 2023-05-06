"""
Counter
Например есть набор температур за первые 15 дней января. Найти количество общих температур,
наиболее частую
"""

import collections

temperatures = [0.5, 0.0, -3.5, -2.5, 1, 1, -1, 0.5, 1.5, -4, -5, -4, 0.5, 1, 0.5]

t_count = collections.Counter(temperatures)
print(t_count)
print(t_count.most_common())
