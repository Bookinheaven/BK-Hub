

import turtle

pen = turtle.Turtle()

# Method 1
# pen.right(120)
# pen.forward(300)
# pen.left(120)
# pen.forward(300)

# pen.left(120)
# pen.forward(50)
# pen.left(60)
# pen.forward(250)
# pen.backward(250)

# for i in range(3):
#     pen.right(60)
#     pen.forward(50)
#     pen.left(60)
#     pen.forward(200 - 50*i)
#     pen.backward(200 - 50*i)

# pen.right(60)
# pen.forward(100)

for _ in range(3):
    pen.forward(300)
    pen.left(120)

pen.left(60)
pen.forward(50)

pen.right(60)
pen.forward(250)

pen.left(120)
pen.forward(50)

pen.left(60)
pen.forward(200)

pen.right(120)
pen.forward(50)

pen.right(60)
pen.forward(150)

pen.left(120)
pen.forward(50)
pen.left(60)
pen.forward(100)


turtle.done()