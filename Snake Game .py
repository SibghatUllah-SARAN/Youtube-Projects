import turtle
import time
import random

# Screen
wn = turtle.Screen()
wn.title("🐍 Snake Game | CodeNovaX Style")
wn.bgcolor("#0f172a")
wn.setup(width=800, height=700)
wn.tracer(0)

# Border
border = turtle.Turtle()
border.hideturtle()
border.speed(0)
border.color("#38bdf8")
border.pensize(5)
border.penup()
border.goto(-390, -340)
border.pendown()
for _ in range(2):
    border.forward(780)
    border.left(90)
    border.forward(680)
    border.left(90)

# Head
head = turtle.Turtle()
head.shape("circle")
head.color("#22c55e")
head.penup()
head.goto(0, 100)
head.direction = "Stop"

# Food
food = turtle.Turtle()
food.shape("circle")
food.color("#ef4444")
food.penup()
food.goto(0, 0)

segments = []

# Score
score = 0
pen = turtle.Turtle()
pen.hideturtle()
pen.color("#e5e7eb")
pen.penup()
pen.goto(0, 300)
pen.write("Score: 0", align="center", font=("Poppins", 24, "bold"))

# Movement
def move():
    if head.direction == "Up":
        head.sety(head.ycor() + 20)
    if head.direction == "Down":
        head.sety(head.ycor() - 20)
    if head.direction == "Left":
        head.setx(head.xcor() - 20)
    if head.direction == "Right":
        head.setx(head.xcor() + 20)

def go_up():
    if head.direction != "Down":
        head.direction = "Up"

def go_down():
    if head.direction != "Up":
        head.direction = "Down"

def go_left():
    if head.direction != "Right":
        head.direction = "Left"

def go_right():
    if head.direction != "Left":
        head.direction = "Right"

# Keyboard
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Main Game Loop
while True:
    wn.update()

    # Wall Collision
    if head.xcor() > 370 or head.xcor() < -370 or head.ycor() > 320 or head.ycor() < -320:
        time.sleep(1)
        head.goto(0, 100)
        head.direction = "Stop"
        for seg in segments:
            seg.goto(1000, 1000)
        segments.clear()
        score = 0
        pen.clear()
        pen.write("Score: 0", align="center", font=("Poppins", 24, "bold"))

    # Food Collision
    if head.distance(food) < 20:
        x = random.randint(-360, 360)
        y = random.randint(-310, 310)
        food.goto(x, y)

        segment = turtle.Turtle()
        segment.shape("circle")
        segment.color("#4ade80")
        segment.penup()
        segments.append(segment)

        score += 10
        pen.clear()
        pen.write(f"Score: {score}", align="center", font=("Poppins", 24, "bold"))

    # Move body
    for i in range(len(segments)-1, 0, -1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x, y)

    if len(segments) > 0:
        segments[0].goto(head.xcor(), head.ycor())

    move()
    time.sleep(0.1)