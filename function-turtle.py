import turtle
turtle.shape('turtle')
turtle.color('green')
turtle.speed(1)

def draw_square(side_length, draw_angle):
    for i in range(4):
        turtle.forward(side_length)
        turtle.left(draw_angle)

counter = 0
while counter < 36:
    draw_square(100, 90)
    turtle.right(10)
    counter += 1

turtle.hideturtle()
turtle.exitonclick()
print('program terminated!')
