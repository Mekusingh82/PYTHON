import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")

dot = turtle.Turtle()
dot.shape("circle")
dot.penup
dot.speed(0)

score = 0
colors = ["red", "blue", "green", "yellow", "pink", "cyan"]

def move():
    global score
    score += 1 
    dot.color(random.choice(colors))
    dot.goto(random.randint(-200, 200), random.randint(-150, 150))

dot.onclick(lambda x, y: move())

for i in range(50):
    dot.shapesize(1.5)
    screen.update()

turtle.done()