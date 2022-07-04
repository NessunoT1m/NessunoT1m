import turtle

turtle.speed(3)
turtle.bgcolor('black')
turtle.pensize(3)

def arc():
    for _ in range(200):
        turtle.right(1)
        turtle.forward(1)


turtle.color('red')
turtle.begin_fill()

turtle.left(140)
turtle.forward(111.65)

arc()
turtle.left(120)

arc()
turtle.forward(111.65)

turtle.hideturtle()
turtle.end_fill()

turtle.done

input()
