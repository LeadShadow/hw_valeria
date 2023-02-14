'''
Запись в файл pathlib
'''

from pathlib import Path

list_data = ['First line\n', 'Second line\n', 'Hello world\n', 'Aloha! Guys\n', 'Last line']
folder = Path('C:/Users/pc/Desktop/заняття/hw_valeria/lesson9')

with open(folder / 'data.txt', 'w', encoding='utf-8') as file:
    for line in list_data:
        file.write(f'{line}')


with open(folder / 'data-all.txt', 'w', encoding='utf-8') as file:
    file.writelines(list_data)