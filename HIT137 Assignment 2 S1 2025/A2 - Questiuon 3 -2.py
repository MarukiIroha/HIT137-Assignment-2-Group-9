import turtle as trl

while True:
    try:
        L_angle = float(input("Please enter left branch angle (must be between -90 and 0): "))
        if -90 <= L_angle <= 0:
            break
        else:
            print(" Invalid value. Please enter a number between -90 and 0.")
    except ValueError:
        print(" Please enter a valid number.")
while True:
    try:
        R_angle = float(input("Please enter right branch angle (must be between 0 and 90): "))
        if 0 <= R_angle <= 90:
            break
        else:
            print(" Invalid value. Please enter a number between 0 and 90.")
    except ValueError:
        print(" Please enter a valid number.")
while True:
    try:
        reduction = float(input("Please enter branch length reduction factor (must be between 0 and 1): "))
        if 0 < reduction < 1:
            break
        else:
            print(" Invalid value. Please enter a float between 0 and 1.")
    except ValueError:
        print(" Please enter a valid number.")
while True:
    try:
        S_length = int(input("Please enter starting branch length (must be between 0 and 200): "))
        if 0 < S_length <= 200:
            break
        else:
            print(" Invalid value. Please enter a float between 0 and 200.")
    except ValueError:
        print(" Please enter a valid number.")

depth = int(input("Please enter recursion depth : "))


def draw_branch(t, S_length, depth):
    if depth == 0:
        return
    t.pensize(depth)
    t.forward(S_length)
    x, y = t.pos()
    heading = t.heading()

    for angle in [L_angle,R_angle]: 
        t.penup()
        t.pencolor(0.0,1.0,0.0)
        t.goto(x, y)
        t.setheading(heading)
        t.left(angle)
        t.pendown()
        draw_branch(t, S_length * reduction, depth - 1)


t = trl.Turtle()
t.speed(0)
t.pencolor((1.0, 0.0, 0.0))
t.left(90)
t.penup()
t.goto(0,-300)
t.pendown()
draw_branch(t, S_length, depth)
t.pencolor(0.0,1.0,0.0)

trl.done()
