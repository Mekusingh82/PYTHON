import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Python Turtle Animation")

pen = turtle.Turtle()
pen.speed(0)

colors = ["blue", "red", "blue", "red"]

for x in range(600):
    pen.pencolor(colors [x % 4])
    pen.width(x // 100 + 1)
    pen.forward(x)
    pen.left(100)

turtle.done()