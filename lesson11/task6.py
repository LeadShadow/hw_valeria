""""
Робота з файлами середовища pathlib
"""

from pathlib import Path

filetext = Path('Test/my_text_file.txt')

filetext.write_text('Fist block\nSecond block\nThird block')
print(filetext.read_text())


