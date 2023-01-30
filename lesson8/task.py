this_is_string = 'Hi didn\'t'

this_is_same = "Hi didn't"

print(this_is_string == this_is_same)

text = """
Як умру, то поховайте

Мене на могилі

Серед степу широкого

На Вкраїні милій,

Щоб лани широкополі,

І Дніпро, і кручі

Було видно, було чути,

Як реве ревучий.

Як понесе з України

У синєє море

Кров ворожу... отойді я

І лани і гори —

Все покину, і полину

До самого Бога

Молитися... а до того

Я не знаю Бога.

Поховайте та вставайте,

Кайдани порвіте

І вражою злою кров’ю

Волю окропіте.

І мене в сем’ї великій,

В сем’ї вольній, новій,

Не забудьте пом’янути

Незлим тихим словом.
"""

print(text)

print(('spam ' 'eggs') == 'spam eggs')
# \n -> переведення рядка
# \f -> переведення сторінки
# \r -> повернення каретки
# \t -> горизонтальна табуляція
# \v -> вертикальна табуляція
# \ -> екрануючий символ

if 10 == 10:
  print('hello world')


s = 'Hi there!'

start = 0
end = 7
print(s.find('er', start, end))
print(s.find('q'))
print(s.index('er'))
# print(s.index('q'))

s = 'Im learning strings in Python. Some new methods got now'
sentences = s.split('. ')

print(sentences[0])
print(sentences[1])


text = '. '.join(sentences)
print(text == s)
print(text)

clean = '   some'.strip()
print(clean)

dogs_text = 'All dogs bark like dogs.'
cats_text = dogs_text.replace('dogs', 'cats')
print(cats_text)

print('TestDog'.removeprefix('Test'))
print('TestDog'.removeprefix('Dog'))

print('TestDog'.removesuffix('Dog'))
print('TestDog'.removesuffix('Test'))


# презентація -> presentacia
map = {ord('п'): 'p', ord('ю'): 'u'}
translated = 'пю'.translate(map)
print(translated)