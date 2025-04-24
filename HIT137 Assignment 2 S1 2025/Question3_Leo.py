# Question 3 - Recursive Tree in Colab (ColabTurtlePlus version)
!pip install ColabTurtlePlus -q
from ColabTurtlePlus import Turtle

Turtle.initializeTurtle()
Turtle.speed(10)
Turtle.setheading(90)

def draw_branch(length, depth, angle_left, angle_right, scale):
    if depth == 0:
        return
    Turtle.forward(length)
    Turtle.left(angle_left)
    draw_branch(length * scale, depth - 1, angle_left, angle_right, scale)
    Turtle.right(angle_left + angle_right)
    draw_branch(length * scale, depth - 1, angle_left, angle_right, scale)
    Turtle.left(angle_right)
    Turtle.backward(length)

# 示例参数
angle_left = 20
angle_right = 25
length = 100
depth = 5
scale = 0.7

draw_branch(length, depth, angle_left, angle_right, scale)
