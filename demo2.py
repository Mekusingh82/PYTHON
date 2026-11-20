import turtle
import colorsys

# 1. Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(800, 800)
turtle.tracer(0, 0) # Smooth animation

# 2. Turtle setup
t = turtle.Turtle()
t.hideturtle()
t.width(2)

rotation = 0

# 3. Animation loop
while True:
    t.clear()
    
    # Draw the rotating flower pattern
    for i in range(150):
        # Shifting colors
        hue = i / 150
        t.pencolor(colorsys.hsv_to_rgb(hue, 1.0, 1.0))
        
        t.up()
        t.goto(0, 0)
        t.down()
        
        # Set heading with rotation factor
        t.setheading(i * 15 + rotation)
        
        # Draw a beautiful curved petal
        t.forward(i)
        t.circle(i * 0.5, 90) # Creates the spiral flower curves
        
    turtle.update()
    rotation += 2 # Increase this number to make it spin faster

turtle.done()
