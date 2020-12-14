# art square by function...
import turtle
turtle.speed(1)
turtle.shape('turtle')
turtle.color('orange')

def square(forward, turn):
    for i in range(4):
        turtle.forward(forward)
        turtle.left(turn)

square(100, 90)
turtle.hideturtle()
turtle.exitonclick()
print('program terminated!')
