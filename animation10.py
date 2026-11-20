import turtle
import colorsys

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(800, 800)
screen.title("Hypnotic Spiral")

t = turtle.Turtle()
t.speed(0)
t.width(2)
t.hideturtle()
h = 0

for i in range(200):
    color = colorsys.hsv_to_rgb(h, 1, 1)
    t.pencolor(color)
    t.forward(i * 1.2)
    t.right(30)
    t.backward(i * 1.2)
    t.left(10)
    h += 0.004
turtle.done() 