# Метод sub


import re

string = 'The best language is C++'

result = re.sub(r'C\+\+', 'Python', string)
print(result)



string = 'blue socks and red shoes'
result = re.sub(r'(blue|white|red)', 'colour', string)
print(result)