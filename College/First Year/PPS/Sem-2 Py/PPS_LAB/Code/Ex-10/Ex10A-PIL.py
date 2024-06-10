"""
Create a program to load an image and demonstrate the following operations on it
a) Display the image
b) Plot the image in console window
c) Display the image size(width and height)
d) Reduce the Image size of its half size
e) Rotate the image 145 degrees
f) Resize the image with 50 units in x direction and 70 units in y direction
g) Flip the image (Left to Right, Top to Bottom)
h) Crop the image
i) Change the color image to GrayScale, Black and White
j) Apply blur effect on the image"""


from PIL import Image, ImageFilter

display = Image.open(r"C:\Users\burnk\Downloads\spell.jpg")
display.show()

path = input("Enter path: ")
img = Image.open(f'{path}')
img.show()
print(f"Height: {display.height} width: {display.width}")
halfsize = display.resize(size=(int(display.height/2),int(display.width/2)))
halfsize.show()
rotate = display.rotate(145)
rotate.show()
rsize = display.resize(size=(50, 70))
rsize.show()
Fliplr = display.transpose(Image.FLIP_LEFT_RIGHT)
Fliplr.show()
Fliptb = display.transpose(Image.FLIP_TOP_BOTTOM)
Fliptb.show()
cr = display.crop((20, 30, 100, 100))
cr.show()
gray = display.convert(mode='LA')
gray.show()
black = display.convert(mode='L')
black.show()
bl = display.filter(ImageFilter.GaussianBlur(radius=5))
bl.show()