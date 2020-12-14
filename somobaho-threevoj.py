#Python program for drawing equilateral triangles...

import turtle
turtle.shape('turtle')
turtle.color('orange')

def triangle(baho, left):
    for i in range(3):
        turtle.forward(baho)
        turtle.left(left)
triangle(150, 120)

turtle.hideturtle()
turtle.exitonclick()
