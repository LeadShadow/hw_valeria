# Реализуйте функцию file_operations(path, additional_info, start_pos, count_chars),
# которая добавляет дополнительную информацию в файл по пути path из параметра additional_info,
# и после этого возвращает строку с позиции start_pos длиной count_chars.
# 'a' -> append
# Требования:
#
# функция должна открывать файл с помощью with по пути path в режиме добавления информации
# записывать в конец файла строку additional_info
# после записи функция должна открыть тот же файл для чтения
# прочитать и вернуть строку с позиции start_pos длиной count_chars с помощью функции seek.
# Важно: для прохождения задачи необходимо использовать менеджер контекста with, методы seek,
# write и read.
# 'a'
# Sasha123
from pathlib import Path

p = Path('task3.txt')

def file_operations(path: Path, additional_info: str, start_pos: int, count_chars: int):
    with open(path, 'a', encoding='utf-8') as file, open(path, 'r', encoding='utf-8') as fh:
        file.write(additional_info)
        fh.seek(start_pos)
        result = fh.read(count_chars)
    return result


if __name__ == "__main__":
    print(file_operations(p, 'I like play computer games', 3, 10))