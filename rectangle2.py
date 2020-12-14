import turtle
turtle.shape('turtle')
turtle.color('green')
turtle.speed(1)

def rectangle():
    for i in range(1):
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(100)

rectangle()
turtle.hideturtle()
turtle.exitonclick()
