# Виберіть будь-яку папку на своєму пк, яка має вложенні директорії. Вивести на прінт
# в термінал її зміст

import pathlib as pt

p = pt.Path('Test')

def parse_file(path: pt.Path):
    for el in path.iterdir():
        if el.is_dir():
            parse_file(el)  # C:/Users/pc/Desktop/заняття/hw_valeria/lesson11/Test/Temp
        else:
            print(f'this is file: {el.name}') # C:/Users/pc/Desktop/заняття/hw_valeria/lesson11/Test/my_bin.bin -> my_bin.bin


def parse_file_glob(path: pt.Path):
    for el in path.glob('**/*'):
        if el.is_file():
            print(f'this is file: {el.name}')


if __name__ == "__main__":
    parse_file(p)
    print('--------------------')
    parse_file_glob(p)