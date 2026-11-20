import math
import random
import time
import turtle

SLOW = 0
FAST = SLOW / 2
JITTER = 0.25
STEP = 5
SC = 0.6

W, H = 752, 1344
CX, CY = W / 2, 670

BG = "#14081a"
GOLD = "#d9b45a"
GOLD_D = "#8a6420"
PINK = "#f2a0ae"

random.seed()

screen = turtle.Screen()
screen.setup(int(W * SC) + 30, int(H * SC) + 30)
screen.bgcolor(BG)
screen.title("Geometry Heart")
screen.tracer(0, 0)

pen = turtle.Turtle(visible=False)
pen.speed(0)
pen.penup()


def to_t(x, y):
    return (x - CX) * SC, (y - CY) * SC