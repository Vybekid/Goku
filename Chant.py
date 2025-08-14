import turtle
import colorsys

turtle.tracer(9)
turtle.bgcolor('black')
turtle.pensize(2)

def draw_hypnotic_spiral():
    h = 0.0  
    for i in range(200):
        c = colorsys.hsv_to_rgb(h, 1, 1)
        
        turtle.pencolor(c)
        
        turtle.fd(i)
        turtle.rt(144)
        
        for _ in range(5):
            turtle.fd(i * 2)  
            turtle.rt(144)    
        
        h += 0.005

draw_hypnotic_spiral()

turtle.done()