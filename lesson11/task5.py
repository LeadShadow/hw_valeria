"""
Запис в файл pathlib
"""
from pathlib import Path

list_data = ['First line\n', 'Hello world!\n', 'Hi guys!\n', 'Last line']

folder = Path('Temp')
# folder / 'test.txt' -> Temp/test.txt
with open(folder / 'test.txt', 'w', encoding='utf-8') as fh:
    for line in list_data:
        fh.write(line)

with open(folder / 'test1.txt', 'w', encoding='utf-8') as fh:
    fh.writelines(list_data)

