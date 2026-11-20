import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Rotating Colorful Animation")

t = turtle.Turtle()
t.speed(0)
t.width(3)

colors = ["red", "orange", "yellow", "green", "cyan", "blue", "purple", "pink"]

for i in range(360):
    t.pencolor(colors[i % len(colors)])
    t.forward(i * 2)
    t.right(59)

turtle.done()