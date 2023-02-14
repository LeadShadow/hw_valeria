# a = 'hello world'
# b = input('')

# файловий дескриптор
file = open('test_file.txt')
file.close()

'''
r -> відкриття на читання(значення за замовчуванням)
w -> відкриття на запис, зміст файлу видаляється, якщо файлу не існує, створюється новий
x -> відкриття на запис, якщо файлу не існує, виникає помилка
a -> відкриття на дозапис, інформація додається в кінець файлу
b -> відкриття в бінарному вигляді(0101010101010010101010101010101101010)
t -> відкриття в текстовому режимі(аналог r, значення за замовчуванням)
+ -> відкриття на читання і на запис
'''


file = open('test.txt', 'w', encoding='utf-8')
symbols = file.write('hello!')
print(symbols)
file.close()

file = open('test_file.txt', 'w+', encoding='utf-8')
file.write('hello!')
file.seek(0)

first_two_symbols = file.read(2)
print(first_two_symbols)
file.close()


file = open('test.txt', 'w', encoding='utf-8')
file.write('hello world!')
file.close()

file = open('test.txt', 'r', encoding='utf-8')
all_file = file.read()
print(all_file)
file.close()

file = open('test.txt', 'w', encoding='utf-8')
file.write('hello world!!!')
file.close()


file = open('test.txt', 'r', encoding='utf-8')
while True:
    symbol = file.read(1)
    if len(symbol) == 0:
        break
    print(symbol)

file.close()

file = open('test.txt', 'w', encoding='utf-8')
file.write('first line\nsecond line\nthird line')
file.close()

file = open('test.txt', 'r', encoding='utf-8')
while True:
    line = file.readline()
    if not line:
        break
    print(line, end='')

file.close()

file = open('test.txt', 'w', encoding='utf-8')
file.write('first line\nsecond line\nthird line')
file.close()

file = open('test.txt', 'r', encoding='utf-8')
lines = file.readlines()
print()
print(lines)
file.close()


# небажаний синтаксис
# file = open('test1.txt')
# try:
#     line = file.read()
# finally:
#     file.close()

with open('test.txt', 'w+') as file:
    file.write('hello')

