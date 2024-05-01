import turtle
pen = turtle.Turtle()
# pen.speed(1000)
# Center of the screen (for my pc)
pen.penup()
pen.setposition(x=-200, y=100)
pen.pendown()

for i in range(8):
    for x in range(8):
        if x % 2 == 0:
            pen.color('black', 'white')
        else:
            pen.color('black', 'brown')
        pen.begin_fill()
        for _ in range(4):
            pen.forward(50)
            pen.right(90)
        pen.end_fill()
        pen.forward(50)
    if i % 2 == 0:
        pen.right(90)
        pen.forward(100)
        pen.right(90)
    else:
        pen.left(180)
turtle.done()