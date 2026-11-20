import turtle
import math
import colorsys
import time

# Screen setup
screen = turtle.Screen()
screen.setup(800, 800)
screen.bgcolor("black")
screen.title("Rainbow Flower Animation")
screen.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(1)

# Animation settings
PETALS = 16
LAYERS = 8
LENGTH = 230
WIDTH = 65

rotation = 0

def rainbow_color(hue):
    r, g, b = colorsys.hsv_to_rgb(hue % 1, 1, 1)
    return (r, g, b)

# Draw one petal
def draw_petal(angle, layer, hue):

    scale = 0.45 + (layer / LAYERS) * 0.55

    pen.penup()

    for i in range(101):
        t = math.pi * i / 100

        x = LENGTH * scale * math.sin(t)
        y = WIDTH * scale * math.sin(t) * math.cos(t)

        # Rotate petal
        a = math.radians(angle)

        rx = x * math.cos(a) - y * math.sin(a)
        ry = x * math.sin(a) + y * math.cos(a)

        if i == 0:
            pen.goto(rx, ry)
            pen.pendown()
        else:
            pen.goto(rx, ry)

    pen.penup()

# Draw complete flower
def draw_flower(rotation):

    pen.clear()

    for p in range(PETALS):

        angle = p * (360 / PETALS) + rotation

        hue = p / PETALS

        for layer in range(LAYERS):

            color = rainbow_color(hue + layer * 0.012)

            pen.pencolor(color)

            draw_petal(angle, layer, hue)

    # Center circle
    pen.penup()
    pen.goto(0, -38)
    pen.pendown()
    pen.pencolor("black")
    pen.fillcolor("black")
    pen.begin_fill()
    pen.circle(38)
    pen.end_fill()
    pen.penup()

# Main animation loop
while True:

    draw_flower(rotation)

    screen.update()

    rotation += 0.35

    time.sleep(0.03)