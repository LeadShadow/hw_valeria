from pathlib import Path
import shutil
import sys
from normalize import normalize
import file_parser as parser


def handler(filename: Path, target_folder: Path):
    # Створюємо папку
    target_folder.mkdir(exist_ok=True, parents=True)
    # Замінюємо шлях до файлу + перетворюємо кирилицю на латиницю
    filename.replace(target_folder / normalize(filename.name))  # борщ -> borch

def handler_archive(filename: Path, target_folder: Path):
    # Створюємо папку для архівів
    target_folder.mkdir(exist_ok=True, parents=True)
    # Створюємо папку і розпаковуємо туди архів
    # Беремо суфікс у файла і забираємо replace(filename.suffix, '')
    folder_for_file = target_folder / normalize(filename.name.replace(filename.suffix, ''))

    # створюємо папку для архіву з іменем файла
    folder_for_file.mkdir(exist_ok=True, parents=True)
    try:
        shutil.unpack_archive(str(filename.resolve()), str(folder_for_file.resolve()))
    except shutil.ReadError:
        print(f'Це не архів! {filename.name}')
        folder_for_file.rmdir()
        return None
    filename.unlink()


def handler_folders(folder: Path):
    try:
        folder.rmdir()
    except OSError:
        print(f'Не вдалось видалити папку {folder.name}')


def main(folder: Path):
    parser.scan(folder)

    for file in parser.JPEG_IMAGES:
        handler(file, folder / 'images' / 'JPEG')
    for file in parser.JPG_IMAGES:
        handler(file, folder / 'images' / 'JPG')
    for file in parser.PNG_IMAGES:
        handler(file, folder / 'images' / 'PNG')
    for file in parser.SVG_IMAGES:
        handler(file, folder / 'images' / 'SVG')

    for file in parser.MP3_AUDIO:
        handler(file, folder / 'audio' / 'MP3')
    for file in parser.OGG_AUDIO:
        handler(file, folder / 'audio' / 'OGG')
    for file in parser.WAV_AUDIO:
        handler(file, folder / 'audio' / 'WAV')
    for file in parser.AMR_AUDIO:
        handler(file, folder / 'audio' / 'AMR')

    for file in parser.MP4_VIDEO:
        handler(file, folder / 'video' / 'MP4')
    for file in parser.MKV_VIDEO:
        handler(file, folder / 'video' / 'MKV')
    for file in parser.MOV_VIDEO:
        handler(file, folder / 'video' / 'MOV')
    for file in parser.AVI_VIDEO:
        handler(file, folder / 'video' / 'AVI')

    for file in parser.PPTX_DOCUMENTS:
        handler(file, folder / 'documents' / 'PPTX')
    for file in parser.TXT_DOCUMENTS:
        handler(file, folder / 'documents' / 'TXT')
    for file in parser.DOC_DOCUMENTS:
        handler(file, folder / 'documents' / 'DOC')
    for file in parser.DOCX_DOCUMENTS:
        handler(file, folder / 'documents' / 'DOCX')
    for file in parser.PDF_DOCUMENTS:
        handler(file, folder / 'documents' / 'PDF')
    for file in parser.XLSX_DOCUMENTS:
        handler(file, folder / 'documents' / 'XLSX')

    for file in parser.OTHER:
        handler(file, folder / 'OTHERS')
    for file in parser.ARCHIVES:
        handler_archive(file, folder / 'ARCHIVES')

    for folder in parser.FOLDERS[::-1]:
        handler_folders(folder)


if __name__ == "__main__":
    if sys.argv[1]:
        folder_for_scan = Path(sys.argv[1])
        print(f'Start in folder {folder_for_scan.resolve()}')
        main(folder_for_scan.resolve())