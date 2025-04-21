import turtle as trl


def branch(t, length, depth):
    if depth == 0:
        return
    t.pensize(depth)
    t.forward(length)
    x, y = t.pos()
    heading = t.heading()

    for angle in [-20, 25]: 
        t.penup()
        t.pencolor(0.0,1.0,0.0)
        t.goto(x, y)
        t.setheading(heading)
        t.left(angle)
        t.pendown()
        branch(t, length * 0.7, depth - 1)


t = trl.Turtle()
t.speed(1)
t.pencolor((1.0, 0.0, 0.0))
t.left(90)
t.penup()
t.goto(0,0)
t.pendown()
branch(t, 100, 5)
t.pencolor(0.0,1.0,0.0)
trl.done()
