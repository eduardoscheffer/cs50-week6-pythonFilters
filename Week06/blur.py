from PIL import Image, ImageFilter

before = Image.open("yard.bmp")
after = before.filter(ImageFilter.BoxBlur(10))
after.save("bluredYard.bmp")