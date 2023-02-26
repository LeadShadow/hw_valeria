import shutil


archive_name = shutil.make_archive('backup', 'zip', 'dist')
shutil.unpack_archive(archive_name)

for s, d in shutil.get_archive_formats():
    print('{:<10} | {:<10}'.format(s, d))
