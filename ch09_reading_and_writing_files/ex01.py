from pathlib import Path
import os

# Backslash - Forward slash
print(Path('spam', 'bacon', 'eggs'))
print(str(Path('spam', 'bacon', 'eggs')))

myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    print(Path(r'/tmp', filename))

cwd = Path.cwd()
print(Path.cwd())
os.chdir('/tmp')
print(Path.cwd())
os.chdir(cwd)

# The home directory
print(Path.home())

# Create new folders
os.makedirs(r'/tmp/delicious/walnut/waffles', exist_ok=True)

Path(r'/tmp/delicious/walnut/waffles/spam').mkdir(exist_ok=True)

# Absolute and relative paths
print(Path.cwd())
print(Path.cwd().is_absolute())
print(Path('spam/bacon/eggs').is_absolute())

print(os.path.abspath('.'))
print(os.path.abspath('.\Scripts'))
print(os.path.isabs('.'))
print(os.path.isabs(os.path.abspath('.')))

print(os.path.relpath(r'/tmp/delicious/walnut/waffles', r'/tmp'))
print(os.path.relpath(r'/tmp/delicious/walnut/waffles', r'/var'))

# Getting the parts of a file path
p = Path('/tmp/spam.txt')
print(p.anchor)
print(p.parent)
print(p.name)
print(p.stem)
print(p.suffix)
print(p.drive)

print(Path.cwd())
print(Path.cwd().parents[0])
# print(Path.cwd().parents[1])
# print(Path.cwd().parents[2])

calcFilePath = r'/tmp/calc'
print(os.path.basename(calcFilePath))
print(os.path.dirname(calcFilePath))
print(os.path.split(calcFilePath))
print(calcFilePath.split(os.sep))

# Finding file sizes and folder contents
print(os.path.getsize(r'/bin/uname'))
print(os.listdir(r'/bin'))

totalSize = 0
for filename in os.listdir(r'/tmp'):
    totalSize += os.path.getsize(os.path.join(r'/tmp', filename))
print(totalSize)

# Modifying a list of files using glob patterns
p = Path('/tmp')
p = Path.home()
print(p.glob('*'))              # generator
print(list(p.glob('*')))        # list
print(list(p.glob('*.txt')))    # list
print(list(p.glob('*.log')))    # list

for textFilePathObj in p.glob('*.txt'):
    print(textFilePathObj)

# Checking Path Validity
optDir = Path('/opt')
notExistsDir = Path('/folder/does/not/exist')
unameFile = Path('/bin/uname')
print(optDir.exists())
print(optDir.is_dir())
print(notExistsDir.exists())
print(unameFile.is_file())
print(unameFile.is_dir())

# The File reading writing process
from pathlib import Path
p = Path('spam.txt')
print(p.write_text('Hello, world!'))
print(p.read_text())

helloFile = open(Path.home() / 'hello.txt')
helloContent = helloFile.read()
print(helloContent)

baconFile = open('bacon.txt', 'w')
baconFile.write('Hello, world!\n')
baconFile.close()
baconFile = open('bacon.txt', 'a')
baconFile.write('Bacon is not a vegetable.')
baconFile.close()
baconFile = open('bacon.txt')
content = baconFile.read()
baconFile.close()
print(content)

# Saving variables with the shelve module
import shelve
shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()

shelfFile = shelve.open('mydata')
print(type(shelfFile))
print(shelfFile['cats'])
shelfFile.close()
print('-' * 40)
shelfFile = shelve.open('mydata')
print(list(shelfFile.keys()))
print(list(shelfFile.values()))
shelfFile.close()

print('-' * 40)
import pprint
cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
pprint.pformat(cats)
fileObj = open('myCats.py', 'w')
fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
fileObj.close()

print('-' * 40)
import myCats
print(myCats.cats)
print(myCats.cats[0])
print(myCats.cats[0]['name'])
