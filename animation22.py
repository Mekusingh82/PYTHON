import turtle
import random

t = turtle.Turtle
s = turtle.Screen()
s.bgcolor("black")
t.speed(0)

for i in range(200):
    t.pencolor("white")
    t.forward(i)
    t.right(144)
    t.circle(i/3)
    t.right(20)

turtle()