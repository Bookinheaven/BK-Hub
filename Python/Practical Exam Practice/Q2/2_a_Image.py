"""
Take an image and do the following image processing
a) Convert an image from RGBA to L mode
b) Rotate the image 5 different angles
c) Paste one image on another image
d) Apply five different filters to the image
"""
import os 
image_path1 = os.path.join(os.path.dirname(__file__), 'image.jpg')
image_path2 = os.path.join(os.path.dirname(__file__), 'image1.jpg')

from PIL import Image, ImageFilter

item = Image.open(image_path1)
item1 = Image.open(image_path2)
# a
blacknwhite = item.convert(mode='L')
# b
rotate1 = item.rotate(40)
rotate2 = item.rotate(80)
rotate3 = item.rotate(120)
rotate4 = item.rotate(160)
rotate5 = item.rotate(200)
#c 
pas = item.copy()
pas.paste(item1,(200,500))
#d
#1
blur = item.filter(ImageFilter.GaussianBlur(radius=10))
#2 
f_edges = item.filter(ImageFilter.FIND_EDGES())
#3
emboss= item.filter(ImageFilter.EMBOSS())
#4
sharpen = item.filter(ImageFilter.SHARPEN())
#5 
smooth = item.filter(ImageFilter.SMOOTH())
for x in [item, blacknwhite, rotate1, rotate2, rotate3, rotate4, rotate5, pas, blur, f_edges, emboss, sharpen, smooth]:
    x.show()