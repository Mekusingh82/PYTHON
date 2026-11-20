
import turtle
import colorsys

# Screen setup
screen = turtle.Screen()
screen.title("Colorful Rotating Flower")
screen.bgcolor("black")
screen.setup(width=900, height=700)
screen.tracer(0)

# Turtle setup
flower = turtle.Turtle()
flower.speed(0)
flower.pensize(2)
flower.hideturtle()

rotation = 0

def draw_flower():
    global rotation

    flower.clear()

    # Draw colorful petals
    for i in range(24):
        hue = i / 24
        color = colorsys.hsv_to_rgb(hue, 1, 1)

        flower.penup()
        flower.goto(0, 0)
        flower.setheading(rotation + i * 15)
        flower.pendown()

        flower.pencolor(color)
        flower.pensize(2)

        flower.circle(90, 60)
        flower.left(120)
        flower.circle(90, 60)
        flower.left(120)

    # Flower center
    flower.penup()
    flower.goto(0, -8)
    flower.dot(18, "yellow")

def animate():
    global rotation

    draw_flower()
    screen.update()

    rotation = (rotation + 3) % 360

    # Repeat animation
    screen.ontimer(animate, 40)

# Press ESC to close
screen.listen()
screen.onkey(screen.bye, "Escape")

# Start animation
animate()
screen.mainloop()
