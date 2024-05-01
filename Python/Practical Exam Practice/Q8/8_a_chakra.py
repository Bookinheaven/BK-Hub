"""
Create a turtle program for the following graphic designs(chakra)
"""
import turtle

pen = turtle.Turtle()
pen.pensize(3)
pen.color('blue')
pen.circle(70)

pen.left(90)
pen.forward(70)
for i in range(24):
    pen.left(15)
    pen.forward(69)
    pen.backward(69)

turtle.done()