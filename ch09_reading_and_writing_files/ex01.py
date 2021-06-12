from pathlib import Path
import os

# Backslash - Forward slash
print(Path('spam', 'bacon', 'eggs'))
print(str(Path('spam', 'bacon', 'eggs')))

myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    print(Path(r'C:\Users\Al', filename))

print(Path.cwd())
# os.chdir('C:\Windows\System32')
print(Path.cwd())

# The home directory
print(Path.home())

# Create new folders
os.makedirs(r'C:\delicious\walnut\waffles', exist_ok=True)

Path(r'C:\delicious\walnut\waffles\spam').mkdir(exist_ok=True)

# Absolute and relative paths
print(Path.cwd())
print(Path.cwd().is_absolute())
print(Path('spam/bacon/eggs').is_absolute())

print(os.path.abspath('.'))
print(os.path.abspath('.\Scripts'))
print(os.path.isabs('.'))
print(os.path.isabs(os.path.abspath('.')))

print(os.path.relpath(r'C:\Windows', r'C:\\' ))
print(os.path.relpath(r'C:\Windows', r'C:\spam\eggs'))

# Getting the parts of a file path
p = Path('C:/Users/Al/spam.txt')
print(p.anchor)                 # C:\
print(p.parent)                 # C:\Users\Al
print(p.name)                   # spam.txt
print(p.stem)                   # spam
print(p.suffix)                 # .txt
print(p.drive)                  # C:

print(Path.cwd())
print(Path.cwd().parents[0])
print(Path.cwd().parents[1])
print(Path.cwd().parents[2])

calcFilePath = r'C:\Windows\System32\calc.exe'
print(os.path.basename(calcFilePath))
print(os.path.dirname(calcFilePath))
print(os.path.split(calcFilePath))
print(calcFilePath.split(os.sep))

# Finding file sizes and folder contents
print(os.path.getsize(r'C:\Windows\System32\calc.exe'))
print(os.listdir(r'C:\Windows\System32'))

totalSize = 0
for filename in os.listdir(r'C:\Windows\System32'):
    totalSize += os.path.getsize(os.path.join(r'C:\Windows\System32', filename))
print(totalSize)

# Modifying a list of files using glob patterns
