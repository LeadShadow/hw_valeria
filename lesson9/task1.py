'''
Метод: search
'''
import re

string = "Нильс Бор родился в семье профессора физиологии Копенгагенского университета Христиана Бора (1858—1911), " \
         "дважды становившегося кандидатом на Нобелевскую премию по физиологии и медицине[10], и Эллен Адлер (" \
         "1860—1930), дочери влиятельного и весьма состоятельного еврейского банкира и парламентария-либерала Давида " \
         "Баруха Адлера (дат. David Baruch Adler; 1826—1878) и Дженни Рафаэль (1830—1902) из британской еврейской " \
         "банкирской династии Raphael Raphael & sons[en][11]. Родители Бора поженились в 1881 году."


result = re.search(r'[0-9]+', string)
print(string.index('1'))
print(result.span())
a, b = result.span()  # 93, 97
print(string[a:b])
print(result.group())
