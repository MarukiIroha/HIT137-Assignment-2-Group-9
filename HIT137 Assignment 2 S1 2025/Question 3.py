"""
Name: Group 9
Date started: 22/04
GitHub URL:https://github.com/MarukiIroha/HIT137-Assignment-2-Group-9/
"""
import turtle


def main():
    try:
        left_angle = float(input("Enter left branch angle (degrees): "))
        right_angle = float(input("Enter right branch angle (degrees): "))
        start_length = float(input("Enter starting branch length (pixels): "))
        depth = int(input("Enter recursion depth: "))
        reduction_factor = float(input("Enter branch length reduction factor (e.g., 0.7 for 70%): "))

        if depth < 0:
            print("Depth must be non-negative.")
            return
        if start_length <= 0:
            print("Starting length must be positive.")
            return
        if reduction_factor <= 0:
            print("Reduction factor must be positive.")
            return
    except ValueError:
        print("Please enter valid numeric values.")
        return

    t = turtle.Turtle()
    screen = turtle.Screen()
    screen.title("Recursive Tree Pattern")

    t.speed(8)
    t.max_depth = depth

    t.penup()
    t.goto(0, -300)  # Match image positioning
    t.setheading(90)
    t.pendown()

    draw_branch(t, start_length, depth, left_angle, right_angle, reduction_factor)


def draw_branch(t, length, depth, left_angle, right_angle, reduction_factor):
    if depth == 0:
        return

    t.pensize(depth)

    if depth == t.max_depth:  # Trunk (first branch)
        t.pencolor(1.0, 0.0, 0.0)  # Red
    else:
        t.pencolor(0.0, 1.0, 0.0)  # Green

    t.forward(length)

    pos = t.position()
    heading = t.heading()

    t.left(left_angle)
    draw_branch(t, length * reduction_factor, depth - 1, left_angle, right_angle, reduction_factor)

    t.penup()
    t.setposition(pos)
    t.setheading(heading)
    t.pendown()

    t.right(right_angle)
    draw_branch(t, length * reduction_factor, depth - 1, left_angle, right_angle, reduction_factor)


if __name__ == "__main__":
    main()