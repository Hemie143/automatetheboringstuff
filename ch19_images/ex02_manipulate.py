from PIL import Image


catIm = Image.open('zophie.png')
print(catIm.size)                       # (816, 1088)
width, height = catIm.size
print(width)                            # 816
print(height)                           # 1088
print(catIm.filename)                   # zophie.png
print(catIm.format)                     # PNG
print(catIm.format_description)         # Portable network graphics
catIm.save('zophie.jpg')

im = Image.new('RGBA', (100, 200), 'purple')
im.save('purpleImage.png')
im2 = Image.new('RGBA', (20, 20))
im2.save('transparentIMage.png')
