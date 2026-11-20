import colorsys
import turtle

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Colorful Rotating Animation")

# Turtle setup
t = turtle.Turtle()
t.speed(0)  # Maximum speed for smooth drawing
t.hideturtle()

# Colors aur animation loop
n = 36
h = 0

turtle.tracer(
    2
)  # Animation ko fast aur smooth banane ke liye frame skipping

for i in range(350):
  # HSV color space se rainbow colors generate karna
  c = colorsys.hsv_to_rgb(h, 1, 1)
  t.pencolor(c)

  # Rotating geometric design patterns
  t.forward(i * 1.5)
  t.left(119)  # Rotation angle jo mesmerizing pattern banata hai
  t.forward(i / 2)
  t.right(60)

  h += 0.008  # Color change speed

# Window ko open rakhne ke liye
turtle.done()