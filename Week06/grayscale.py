from PIL import Image, ImageFilter

before = Image.open("yard.bmp")
after = before.convert('L')
after.save("grayOut.bmp")