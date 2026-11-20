from turtle import *
from colorsys import *

bgcolor("black")
speed(0)
pensize(2)
tracer(5)

h = 0.3
R = 220
r = 67

for layer in range(3):
    d = 90 + layer * 15
    penup()
    for i in range(600):
        theta = (i / 600) * 20 * pi
        x = (R-r)*cos(theta) + d*cos(((R-r)/r)*(theta))
        y = (R-r)*sin(theta) + d*sin(((R-r)/r)*(theta))
        color(hsv_to_rgb(h, 0.9, 1))
        goto(x ,y)
        pendown()
        h = (h + 1/600) % 1
    penup()
hideturtle()
done()