"""
Створення директорій pathlib
"""

from pathlib import Path

new_dir = Path('Tempr')
new_dir.mkdir(exist_ok=True)
new_dir.rmdir()

new_dir = Path('ds1/Test/Temp')
new_dir.mkdir(exist_ok=True, parents=True)