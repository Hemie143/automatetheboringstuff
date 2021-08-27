from PIL import ImageColor


print(ImageColor.getcolor('red', 'RGBA'))               # (255, 0, 0, 255)
print(ImageColor.getcolor('RED', 'RGBA'))               # (255, 0, 0, 255)
print(ImageColor.getcolor('Black', 'RGBA'))             # (0, 0, 0, 255)
print(ImageColor.getcolor('chocolate', 'RGBA'))         # (210, 105, 30, 255)
print(ImageColor.getcolor('CornflowerBlue', 'RGBA'))    # (100, 149, 237, 255)
