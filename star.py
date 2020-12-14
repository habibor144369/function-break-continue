# art square by function...
import turtle
turtle.speed(1)
turtle.shape('turtle')
turtle.color('orange')

def square(forward, turn):
    for i in range(5):
        turtle.forward(forward)
        turtle.right(turn)

square(150, 144)
turtle.hideturtle()
turtle.exitonclick()
print('program terminated!')
