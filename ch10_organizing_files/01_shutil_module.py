import shutil
import os

from pathlib import Path


p = Path('spam.txt')
p.write_text('Hello, world!')

# p = Path.home()
shutil.copy('spam.txt', 'out')
shutil.copy('spam.txt', 'out/spam2.txt')

shutil.copytree('out', 'out2', dirs_exist_ok=True)

p = Path('will_move.txt')
p.write_text('Hello, world!')
shutil.move('will_move.txt', 'moved.txt')

for filename in Path.cwd().glob('*.txt'):
    os.unlink(filename)

import send2trash
baconFile = open('bacon.txt', 'a')
baconFile.write('Bacon is not a vegetable.')
baconFile.close()
send2trash.send2trash('bacon.txt')

