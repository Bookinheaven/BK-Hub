import turtle
pen = turtle.Turtle()
for row in range(8):
    for x in range(8):
        if x % 2 == 0:
            pen.color('black','white')
        else:
            pen.color('black','brown')
        pen.begin_fill() 
        for _ in range(4):
            pen.forward(50)
            pen.right(90)
        pen.end_fill()
        pen.forward(50) 
    if row % 2 == 0:
        pen.right(90)
        pen.forward(100)
        pen.right(90)
    else:
        pen.left(180)
turtle.done()
