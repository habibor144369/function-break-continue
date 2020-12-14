# Rectangle Drawing Python Program
import turtle
turtle.shape('turtle')
turtle.color('orange')

def triangle():
    for i in range(1):
        turtle.forward(200)
        turtle.left(60)
        turtle.forward(120)
        turtle.left(120)
        turtle.forward(200)
        turtle.left(60)
        turtle.forward(120)

triangle()

turtle.hideturtle()
turtle.exitonclick()
