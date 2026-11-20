import turtle

t = turtle.Turtle()
t.speed(0)
t.width(0)

color = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "cyan"]

for i in range(100):
    t.pencolor(color[i % len(color)])
    t.forward(i * 2)
    t.right(91)

tuple.done()