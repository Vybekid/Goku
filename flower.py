import turtle
import math
import colorsys 

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Animated Flower")
screen.tracer(0)

pen = turtle.Turtle()
pen.speed(100)
pen.hideturtle()

def draw_animated_flower():
    angle = 0
    hue = 0
    
    while True:
        color = colorsys.hsv_to_rgb(hue, 1, 1)
        pen.pencolor(color)
        
        pen.clear()
        
        for i in range(2):
            for _ in range(90):
                pen.forward(150)
                pen.left(math.sin(math.radians(angle)) * 50 + 91)
        
        screen.update()
        
        angle += 1
        hue += 0.005
        if hue > 1:
            hue -= 1

try:
    draw_animated_flower()
    turtle.done()
except turtle.Terminator:
    pass