from turtle import *
from colorsys import *

tracer(10)
bgcolor("black")

R = 0
goto(270, -5)

for i in range(250):
    color(hsv_to_rgb(R, 1, 1))
    circle(i, 190)
    forward(65)

circle(220, 90)

done()