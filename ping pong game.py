import turtle

# Screen
wn = turtle.Screen()
wn.title("🏓 Pong Game | CodeNovaX")
wn.bgcolor("#020617")
wn.setup(width=900, height=600)
wn.tracer(0)

# Border
border = turtle.Turtle()
border.speed(0)
border.color("#0ea5e9")
border.penup()
border.goto(-440, -280)
border.pendown()
border.pensize(4)
border.hideturtle()
for _ in range(2):
    border.forward(880)
    border.left(90)
    border.forward(560)
    border.left(90)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.shape("square")
paddle_a.color("#38bdf8")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-400, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.shape("square")
paddle_b.color("#f97316")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(400, 0)

# Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("#22c55e")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.22
ball.dy = 0.22

# Score
score_a = 0
score_b = 0

pen = turtle.Turtle()
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Player A: 0   Player B: 0", align="center", font=("Arial", 22, "bold"))

# Movement
def paddle_a_up():
    paddle_a.sety(paddle_a.ycor() + 30)

def paddle_a_down():
    paddle_a.sety(paddle_a.ycor() - 30)

def paddle_b_up():
    paddle_b.sety(paddle_b.ycor() + 30)

def paddle_b_down():
    paddle_b.sety(paddle_b.ycor() - 30)

# Keyboard
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main Loop
while True:
    wn.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Top & Bottom Collision
    if ball.ycor() > 260 or ball.ycor() < -260:
        ball.dy *= -1

    # Left & Right Goal
    if ball.xcor() > 430:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1

    if ball.xcor() < -430:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1

    # Paddle Collision
    if (340 < ball.xcor() < 350) and paddle_b.ycor()-50 < ball.ycor() < paddle_b.ycor()+50:
        ball.dx *= -1

    if (-350 < ball.xcor() < -340) and paddle_a.ycor()-50 < ball.ycor() < paddle_a.ycor()+50:
        ball.dx *= -1

    # Update Score
    pen.clear()
    pen.write(f"Player A: {score_a}   Player B: {score_b}",
              align="center", font=("Arial", 22, "bold"))
