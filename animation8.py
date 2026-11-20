import turtle
screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(0)
t.width(0)

color = ["red", "pink", "magenta", "hotpink"]

for i in range(120):
    t.color(color[i % len(color)])
    t.begin_fill()

    for _ in range(200):
        t.right(1)
        t.forward(1)

    t.left(120)

    for _ in range(200):
        t.right(1)
        t.forward(1)

    t.forward(111)
    t.end_fill()
    t.right(3)

turtle.done() 