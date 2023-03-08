# Мы имеем следующую структуру файла:
# 60b90c1c13067a15887e1ae1,Tayson,3
# 60b90c2413067a15887e1ae2,Vika,1
# 60b90c2e13067a15887e1ae3,Barsik,2
# 60b90c3b13067a15887e1ae4,Simon,12
# 60b90c4613067a15887e1ae5,Tessi,5
# Каждая запись состоит из трех частей и начинается с новой строки. Например, для первой записи
# начало 60b90c1c13067a15887e1ae1 —
# это первичный ключ базы данных MongoDB. Он всегда содержит 12 байт или ровно 24 символа.
# Дальше мы видим кличку кота Tayson и его возраст 3.
# Все части записи разделены символом запятая ,
#
# Разработайте функцию get_cats_info(path), которая будет возвращать список словарей с данными кошек в виде:
#
# [
#     {"id": "60b90c1c13067a15887e1ae1", "name": "Tayson", "age": "3"},
#     {"id": "60b90c2413067a15887e1ae2", "name": "Vika", "age": "1"},
#     {"id": "60b90c2e13067a15887e1ae3", "name": "Barsik", "age": "2"},
#     {"id": "60b90c3b13067a15887e1ae4", "name": "Simon", "age": "12"},
#     {"id": "60b90c4613067a15887e1ae5", "name": "Tessi", "age": "5"},
# ]
# Параметры функции:
#
# path - путь к файлу
# Требования:
#
# прочтите содержимое файла, используя режим "r".
# мы используем менеджер контекста with
# верните из функции список кошек из файла в требуемом формате


from pathlib import Path
def get_cats_info(path):
    data_cats = list()
    with open(path, "r") as file:
        for line in file:
            if not line:
                break
            line = line.replace('\n', '')
            line_split = line.split(',')
            dict_ = { "id": line_split[0], "name": line_split[1], "age": line_split[2] }
            data_cats.append(dict_)
    return data_cats
    file.close()


if __name__ == "__main__":
    path_ = Path('cats.txt')
    print(get_cats_info(path_))
