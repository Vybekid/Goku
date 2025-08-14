import turtle
import colorsys

# --- Setup the turtle environment ---
# Make the turtle's drawing nearly instant for a quick result
turtle.tracer(300)
# Set a dark background color for a nice contrast
turtle.bgcolor('black')
# Set the turtle's pen size for a thinner line
turtle.pensize(1)
# Hide the turtle icon to just show the drawing
turtle.hideturtle()

def draw_geometric_pattern():
    """
    Draws a complex, colorful geometric pattern using multiple nested loops.
    """
    h = 0.0  # Hue value for color, starts at 0.0 for red
    
    # --- Main loop to draw the overall pattern ---
    # We will draw 200 repetitions of the main shape
    for i in range(200):
        # Convert the current hue to an RGB color
        c = colorsys.hsv_to_rgb(h, 1, 1)
        # Set the color of the pen to the new RGB color
        turtle.pencolor(c)
        
        # --- Inner loop to create the geometric shape ---
        # Draw a shape with 4 sides that gets bigger each time
        for j in range(4):
            turtle.forward(i * 2)
            turtle.right(90) # Turn 90 degrees to form a square
            
        # Move the turtle's position without drawing
        turtle.penup()
        # Move forward slightly to start the next shape
        turtle.forward(5)
        # Turn to rotate the next shape
        turtle.right(1)
        turtle.pendown()

        # Increment the hue for the next color in the spectrum
        h += 0.005

# --- Execute the drawing ---
draw_geometric_pattern()

# --- Keep the window open ---
# This line keeps the graphics window open until you close it manually
turtle.done()
