from PIL import Image, ImageDraw, ImageFont
import os


im = Image.new('RGBA', (200, 200), 'white')
draw = ImageDraw.Draw(im)
draw.text((20, 150), 'Hello', fill='purple')
fontsFolder = '/usr/share/fonts/truetype/freefont'
arialFont = ImageFont.truetype(os.path.join(fontsFolder, 'FreeMono.ttf'), 32)
draw.text((100, 150), 'Howdy', fill='gray', font=arialFont)
im.save('text.png')
