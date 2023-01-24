from pathlib import Path

p = Path()

for i in p.iterdir():
    if i.suffix == '.py':
        print('Це пайтон файл!')
    elif i.suffix == '.docx' or i.suffix == '.doc' or i.suffix == '.txt':
        print('Це текстовий файл!')
    elif i.suffix == '.pdf' or i.suffix == '.jpg':
        print('Це фото!')
    elif i.suffix == '':
        print('Це папка!')
    else:
        print('Інші файли')