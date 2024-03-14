import turtle

main = turtle.Turtle()

main.left(90)
main.forward(150)
main.left(90)
main.color("black","blue")
main.begin_fill()
main.forward(60)
main.right(90)
main.forward(30)
main.right(90)
main.forward(60)
main.left(90)
main.backward(30)
main.end_fill()
main.forward(90)

main.color("black","yellow")
main.begin_fill()
main.right(90)
main.circle(30)
main.end_fill()

turtle.done()