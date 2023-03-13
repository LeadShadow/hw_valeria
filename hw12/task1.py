# Создайте функционал для распаковки архива.
#
# Сделайте import пакета shutil
#
# Создайте функцию unpack(archive_path, path_to_unpack), которая будет вызывать метод
# пакета shutil unpack_archive и распаковывать архив archive_path в место path_to_unpack.
#
# Функция ничего не возвращает.

import shutil

from pathlib import Path

def unpack(archive_path: Path, path_to_unpack: Path):
    shutil.unpack_archive(archive_path, path_to_unpack, 'zip')

unpack(Path('hw12/backup.zip'), Path('C:/Users/pc/Desktop/заняття'))