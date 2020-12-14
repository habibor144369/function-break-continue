# Star topology using python program----
import turtle
turtle.speed(5)
turtle.shape('turtle')
turtle.color('green')

def square(forward, turn):
    for i in range(5):
        turtle.forward(forward)
        turtle.right(turn)
        turtle.forward(forward)

        for i in range(5):
            turtle.forward(forward)
            turtle.right(turn)

square(150, 144)
turtle.hideturtle()
turtle.exitonclick()
print('program terminated!')
