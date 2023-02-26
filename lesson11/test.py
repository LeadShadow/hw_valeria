# pathlib
# .name, .parent, .is_dir(), .is_file(), .exists(), .unlink(), .suffix(), .iterdir(), .glob()


from pathlib import Path

dir_ = Path('C:/Users/pc/Desktop/заняття/hw_valeria/lesson11')

for el in dir_.glob('**/*.txt'):
    print(el)

tmp = Path('test.txt')
tmp.unlink()