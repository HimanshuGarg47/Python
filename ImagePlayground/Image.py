from PIL import Image , ImageFilter
# ImagePlayground\Images\charmander.jpg
img = Image.open(r"D:\myCode\Python\ImagePlayground\Images\astro.jpg")
print(img.size)
img.thumbnail((400,200))
print(img.size)
img.save('thumbnail.png','png')
# filtered_image = img.filter(ImageFilter.BLUR) # ImageFilter.Sharpen etc read documentation
# filtered_image = img.convert('L')
# crooked = filtered_image.rotate(90)
# crooked = filtered_image.resize((100,100))
# box = (100, 100, 400, 400)
# region = filtered_image.crop(box)
# region.save('grey.png','png')
# crooked.save('grey.png','png')
# filtered_image.save('grey.png','png')
# crooked.show()
# print(img.mode)
# print(dir(img))