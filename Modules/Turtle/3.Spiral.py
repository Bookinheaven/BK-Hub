import turtle

screen = turtle.Screen()
pen = turtle.Turtle()

for i in range(100):
    pen.forward(i)
    pen.right(90)

screen.exitonclick()
