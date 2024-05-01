"""
Create a turtle program for printing a star filled with green color
"""
import turtle

pen = turtle.Turtle()
turtle.screensize(1000,1000)

pen.color('yellow', 'green')
pen.begin_fill()
for _ in range(5):
    pen.left(75)
    pen.forward(50)
    pen.right(148)
    pen.forward(50)
pen.end_fill()

turtle.done()