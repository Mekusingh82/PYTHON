import turtle
import colorsys

t = turtle.Turtle()
screen = turtle.Screen()

screen.bgcolor("black")
t.speed(0)
t.width(2)

h = 0

for i in range(360):
    color = colorsys.hsv_to_rgb(h, 1, 1)
    t.pencolor(color)

    t.forward(i * 2)
    t.right(59)
    t.forward(i)
    t.right(121)

    h += 0.003

turtle.done()