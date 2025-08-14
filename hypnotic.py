import turtle
import colorsys
import math

turtle.tracer(10)
turtle.bgcolor('black')
turtle.pensize(2)
turtle.hideturtle()

def draw_hypnotic_swirl():
    num_steps = 700
    h = 0.0

    for i in range(num_steps):
        c = colorsys.hsv_to_rgb(h, 1, 1)
        turtle.pencolor(c)
        
        pen_size = 2 + math.sin(i * 0.1) * 2
        turtle.pensize(pen_size)

        turtle.forward(i * 0.5)
        
        turn_angle = 150 + math.cos(i * 0.1) * 30
        turtle.right(turn_angle)

        h += 0.003
        
        turtle.left(1)

draw_hypnotic_swirl()

turtle.done()