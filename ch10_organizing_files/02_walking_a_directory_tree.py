import os
for folderName, subfolders, filenames in os.walk('/tmp'):
    print(f'The current folder is {folderName}')

    for subfolder in subfolders:
        print(f'SUBFOLDER OF {folderName}: {subfolder}')

    for filename in filenames:
        print(f'FILE INSIDE {folderName}: {filename}')

    print('')

# Reading ZIP files
import zipfile

from pathlib import Path
exampleZip = zipfile.ZipFile('example.zip')
print(exampleZip.namelist())
spamInfo = exampleZip.getinfo('spam.txt')
print(spamInfo.file_size)
print(spamInfo.compress_size)
print(f'Compressed file is {round(spamInfo.file_size / spamInfo.compress_size, 2)}x smaller')
exampleZip.close()

# Extracting from ZIP files
exampleZip = zipfile.ZipFile('example.zip')
exampleZip.extractall()
exampleZip.extract('spam.txt')
exampleZip.extract('spam.txt', './out2/')
exampleZip.close()

# Creating and adding to ZIP files
newZip = zipfile.ZipFile('new.zip', 'w')
newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()
