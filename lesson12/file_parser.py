import sys
from pathlib import Path

JPEG_IMAGES = []
JPG_IMAGES = []
PNG_IMAGES = []
SVG_IMAGES = []
MP3_AUDIO = []
OGG_AUDIO = []
WAV_AUDIO = []
AMR_AUDIO = []
OTHER = []
ARCHIVES = []
AVI_VIDEO = []
MKV_VIDEO = []
MP4_VIDEO = []
MOV_VIDEO = []
DOC_DOCUMENTS = []
DOCX_DOCUMENTS = []
TXT_DOCUMENTS = []
PDF_DOCUMENTS = []
PPTX_DOCUMENTS = []
XLSX_DOCUMENTS = []
FOLDERS = []
EXTENSIONS = set()
UNKNOWN = set()

REGISTER_EXTENSIONS = {
    'JPEG': JPEG_IMAGES,
    'JPG': JPG_IMAGES,
    'SVG': SVG_IMAGES,
    'PNG': PNG_IMAGES,
    'MP3': MP3_AUDIO,
    'OGG': OGG_AUDIO,
    'WAV': WAV_AUDIO,
    'AMR': AMR_AUDIO,
    'GZ': ARCHIVES,
    'TAR': ARCHIVES,
    'ZIP': ARCHIVES,
    'MP4': MP4_VIDEO,
    'AVI': AVI_VIDEO,
    'MKV': MKV_VIDEO,
    'MOV': MOV_VIDEO,
    'DOC': DOC_DOCUMENTS,
    'DOCX': DOCX_DOCUMENTS,
    'PPTX': PPTX_DOCUMENTS,
    'TXT': TXT_DOCUMENTS,
    'PDF': PDF_DOCUMENTS,
    'XLSX': XLSX_DOCUMENTS
}

# audio.mp3 -> MP3
def get_extensions(filename: str) -> str:
    # перетворюємо розширення файлу в назву папки .txt -> TXT
    return Path(filename).suffix[1:].upper()

print(REGISTER_EXTENSIONS[get_extensions('audio.mp3')])


